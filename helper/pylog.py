# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:34:16 2015

@author: muou
"""


import logging
import logging.config

log_format = ["%(message)s", 
              "[%(levelname)s]: %(message)s", 
              "%(asctime)s [%(levelname)s]: %(message)s", 
              "%(asctime)s [%(filename)s-%(levelname)s]: %(message)s", 
              "%(asctime)s [%(filename)s:%(lineno)s-%(levelname)s]: %(message)s"]
log_format_dict = {
    1 : logging.Formatter(log_format[0]),
    2 : logging.Formatter(log_format[1]),
    3 : logging.Formatter(log_format[2]),
    4 : logging.Formatter(log_format[3]),
    5 : logging.Formatter(log_format[4])
}

class Pylog(object):
    def __init__(self, logname="log.txt", level=2, callfile=__file__):
        
        self.RESULT = logging.CRITICAL + 1
        logging.addLevelName(self.RESULT, 'RET')
        logging.basicConfig(level=logging.DEBUG, format=log_format[level-1])
#        self.logger = logging.getLogger(callfile)
#        self.logger.setLevel(logging.DEBUG)
#        
#        #fh = logging.FileHandler(logname)
#
#        ch = logging.StreamHandler()
#        ch.setLevel(logging.DEBUG)
#        ch.setFormatter(log_format_dict[int(loglevel)])
#        #fh.setFormatter(formatter_dict[int(loglevel)])
#        self.logger.addHandler(ch)
        #self.logger.addHandler(fh)
        
    def debug(self, msg, *args, **kwargs):
        logging.log(logging.DEBUG, "%s" % msg, *args, **kwargs)
        
    def info(self, msg, *args, **kwargs):
        logging.log(logging.INFO, "%s" % msg, *args, **kwargs)
        
    def warn(self, msg, *args, **kwargs):
        logging.log(logging.WARN, "%s" % msg, *args, **kwargs)
        
    def error(self, msg, *args, **kwargs):
        logging.log(logging.ERROR, "%s" % msg, *args, **kwargs)
        
    def critical(self, msg, *args, **kwargs):
        logging.log(logging.CRITICAL, "%s" % msg, *args, **kwargs)
        
    def result(self, msg, *args, **kwargs):
        print "-" * (len(msg) + 7)
        logging.log(self.RESULT, "%s" % msg, *args, **kwargs)
        print "-" * (len(msg) + 7)


    def get_logger(self):
        return self.logger


#if __name__ == '__main__':
#    #logger = Logger(logname='log.txt', level=2, callfile=__file__).get_logger()
#    log = Pylog(level=2)
#    #logger = log.get_logger()
#    
#    log.debug('test debug')
#    log.info('test info')
#    log.warn('test warn')
#    log.error('test error')
#    log.result('test reuslt')
#    #logger.critical("test cri")
    
   
