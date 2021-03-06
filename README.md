CoolLogger
==========

Python zipper-rotation Logger, it means it will automagically zip past logs and delete logs older than N days, worry no more about logs disk space.

Installing:

    $ pip install coollogger

USAGE:

```python
    from coollogger import CoolLogger
    import traceback

    logger = CoolLogger(
        log_filename='log.log',
        name='test_logger', # Name of the Logger instance, to avoid Singleton
        keep_zipped = 20    # keep last 20 zipped log files, remove older
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
```

Log file Output:

    2013-08-29 12:21:38,813 - INFO - Logging INFO line
    2013-08-29 12:21:38,813 - WARNING - Warning Logger line
    2013-08-29 12:21:38,813 - ERROR - Module not found
    2013-08-29 12:21:38,813 - ERROR - Logging Exception line None
    Traceback (most recent call last):
      File "example.py", line 23, in <module>
        len(9)
    TypeError: object of type 'int' has no len()


For more information on how to use python logger modules see: http://docs.python.org/2/library/logging.html