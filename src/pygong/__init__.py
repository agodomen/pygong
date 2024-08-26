import os
version = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'pygong.VERSION'), 'r').read().strip()
__version__ = version