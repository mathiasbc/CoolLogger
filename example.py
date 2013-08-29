#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from logger.logger import Logger
import traceback

if __name__ == '__main__':
    logger = Logger(
        log_filename='log.log',
        name='test_logger', # Name of the Logger instance, to avoid Singleton
        keep_zipped = 20    # keep last 20 zipped log files
    ).getLogger()

    logger.info('Logging INFO line')
    logger.warning('Warning Logger line')
    
    try:
        import NonFoudModule
    except ImportError:
        logger.error('Module not found')

    try:
        len(9)
        logger.critical('This will fail len(9)')
    except:
        logger.exception('Logging Exception line %s' % traceback.print_exc())
        pass

