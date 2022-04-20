import time
import logging
filePath='AutoDT-UI/Log'
class Logger(object):
    def __init__(self, logger, CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        currTime = time.strftime("%Y-%m-%d")
        self.logFileName = filePath+r'/Log/log' + currTime + '.log'
        fh = logging.FileHandler(self.logFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)
        self.logger.addHandler(fh)