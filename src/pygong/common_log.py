import errno
from . import io_fcntl
import time
from logging.handlers import TimedRotatingFileHandler
import logging
import os
import threading
import mimetypes


# 创建自定义formatter
class ColoredFormatter(logging.Formatter):
    """
    A formatter that allows colors to be added to the log messages.
    """

    COLOR_CODES = {
        'DEBUG': '\033[1;37m',  # blue\033[94m
        'INFO': '\033[92m',  # green
        'WARNING': '\033[93m',  # yellow
        'ERROR': '\033[91m',  # red
        'CRITICAL': '\033[95m',  # magenta
    }

    def format(self, record):
        log_str = super().format(record)
        color_code = self.COLOR_CODES.get(record.levelname, '')
        reset_code = '\033[0m'
        return color_code + log_str + reset_code

class ConcurrentTimedRotatingFileHandler(TimedRotatingFileHandler):
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        if self.stream:
            self.stream.close()
            self.stream = None
        # get the time that this sequence started at and make it a TimeTuple
        currentTime = int(time.time())
        dstNow = time.localtime(currentTime)[-1]
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        dfn = self.rotation_filename(self.baseFilename + "." +
                                     time.strftime(self.suffix, timeTuple))
        # 兼容多进程并发 LOG_ROTATE
        if not os.path.exists(dfn):
            f = open(self.baseFilename, 'a')
            io_fcntl.lockf(f.fileno(), io_fcntl.LOCK_EX)
            if not os.path.exists(dfn):
                os.rename(self.baseFilename, dfn)
            # 释放锁 释放老 log 句柄
            f.close()
        self.rotate(self.baseFilename, dfn)
        if self.backupCount > 0:
            for s in self.getFilesToDelete():
                os.remove(s)
        if not self.delay:
            self.stream = self._open()
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt

class CommonLogger():
    def __init__(self,file_location="log/prog.log",handler_suffix="%Y%m%d.log",formatter=None):

        if formatter is None:
            formatter = ColoredFormatter('%(asctime)s - %(process)d - %(threadName)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s')

        # 创建控制台输出的Handler
        lock = threading.Lock()
        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.INFO)
        # formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(formatter)



        # 创建文件输出的Handler
        # file_handler = logging.FileHandler('example.log')
        # file_handler.setLevel(logging.DEBUG)
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # file_handler.setFormatter(formatter)

        if not os.path.exists(file_location):
            if mimetypes.guess_type(file_location)[0] is not None or file_location.endswith(".log"):
                location = os.path.dirname(file_location)
            else:
                location = file_location
            try:
                with lock:
                    if not os.path.exists(location):
                        os.makedirs(location)
            except OSError as err:
                if err.errno != errno.EEXIST:
                    raise
                self.file_location = file_location

        self.file_handler = ConcurrentTimedRotatingFileHandler(file_location, when='d', backupCount=7, encoding="utf-8")
        self.file_handler.suffix = handler_suffix
        # ch = logging.StreamHandler()
        # NOTSET->DEBUG->INFO->WARN->ERROR->FATAL->CRITICAL
        self.file_handler.setLevel(logging.INFO)
        self.file_handler.setFormatter(formatter)


    def getFileLogger(self):
        logger.addHandler(self.file_handler)
        return logger

    def getFileLogger(self,file_handler):
        logger.addHandler(file_handler)
        return logger

    def getFileLogger(self,file_handler):
        logger.removeHandler(file_handler)
        return logger
    def removeFileLogger(self):
        logger.removeHandler(self.file_handler)
        return logger

    def getLogger(self):
        logger = logging.getLogger("prog")
        logger.setLevel(logging.DEBUG)

        logger.addHandler(self.console_handler)
        return logger

logger = CommonLogger().getLogger()
def get_logger():
    return logger

