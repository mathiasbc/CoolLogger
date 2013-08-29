CoolLogger
==========

Python zipper-rotation Logger, it means it will automagically zip past logs and delete logs older than N days, worry no more about logs disk space.

USAGE:


    from logger.logger import Logger
    import traceback
    
    logger = Logger(
        log_filename='log.log',
        name='test_logger', # Name of the Logger instance, to avoid Singleton
        keep_zipped = 20    # keep last 20 zipped log files
    ).getLogger()
    logger.info('Logging INFO line')
    logger.warning('Warning Logger line')
    try:
        len(9)
        logger.critical('This will fail len(9)')
    except:
        logger.exception('Logging ERROR line %s' % traceback.print_exc())
        pass


For more information on how to use python logger modules see: http://docs.python.org/2/library/logging.html