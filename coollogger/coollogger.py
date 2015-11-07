import logging, logging.handlers

from TimedCompressedRotatingFileHandler import (
     TimedCompressedRotatingFileHandler
)


class CoolLogger(object):
    ''' Logger class. This class is basedon TimedCompressedRotatingFileHandler 
    which will create a new file every 24 hours, doing a zip of the last log 
    file and storing up to N zipped past files. This class also allows to have
    several logger in the same namespace'''

    def __init__(self, log_filename, name, keep_zipped=50):
        self.LOG_FILENAME = log_filename

        logging.basicConfig(format='%(asctime)s %(message)s')
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        loghandler = TimedCompressedRotatingFileHandler(
            self.LOG_FILENAME, when="midnight", backupCount=keep_zipped
        )
        loghandler.setFormatter(formatter)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(loghandler)

    def getLogger(self):
        ''' return logger handle '''
        return self.logger

    @staticmethod
    def getByName(name):
        '''returns the logger with name'''
        return logging.getLogger(name)

        