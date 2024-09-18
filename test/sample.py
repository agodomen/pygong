"""
Test for module dev usage
"""
# from src import common_log
# from pygong import common_log
# import numpy
# import pygong
# logger = common_log.get_logger()
#
# logger.info("test")
import pygong
from pygong.common_log import logger

print(pygong.__file__)
print(pygong.__version__)
log = pygong.common_log.logger
pygong.common_log.common_logger.open_file_logger(file_location='/tmp/1.log')
log.debug("debug")
log.info("info")
# log.warn("warn")
log.warning("warning")
log.error("error")
# log.exception("exception")
log.critical("critical")
# log.fatal("fatal")

# log.log(level=0,msg="log")
# log.log(level=1,msg="log")
# log.log(level=2,msg="log")
# log.log(level=3,msg="log")
# log.log(level=4,msg="log")
# print('\033[95mThis text is close to fuchsia color.\033[0m')
# print('\033[30;47m This text has black foreground and white background. \033[0m')
# print('\033[30m This text has black foreground only. \033[0m')
# print('\033[40m This text has black background only. \033[0m')