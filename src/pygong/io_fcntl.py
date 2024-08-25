import os
def get_LOCK_EX():
    try:
        import fcntl
        return fcntl.LOCK_EX
    except ImportError:
        if os.name == 'nt':
            return
            # import win32_support
            # import win32_support as fcntl
        else:
            raise
LOCK_EX=get_LOCK_EX()
def fcntl(fd, op, arg=0):
    try:
        import fcntl
        fcntl.fcntl(fd,op,arg)
    except ImportError:
        if os.name == 'nt':
            return 0
            # import win32_support
            # import win32_support as fcntl
        else:
            raise


def ioctl(fd, op, arg=0, mutable_flag=True):
    try:
        import fcntl
        fcntl.ioctl(fd,op,arg,mutable_flag)
    except ImportError:
        if os.name == 'nt':
            if mutable_flag:
                return 0
            else:
                return ""
            # import win32_support
            # import win32_support as fcntl
        else:
            raise


def flock(fd, op):
    try:
        import fcntl
        fcntl.flock(fd,op)
    except ImportError:
        if os.name == 'nt':
            return
            # import win32_support
            # import win32_support as fcntl
        else:
            raise



def lockf(fd, operation, length=0, start=0, whence=0):
    try:
        import fcntl
        fcntl.lockf(fd,operation,length,start,whence)
    except ImportError:
        if os.name == 'nt':
            return
            # import win32_support
            # import win32_support as fcntl
        else:
            raise
