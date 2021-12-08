import logging

'''
levels
-debug
-info
-warning
-error
-critical (program might not continue => serious error)
'''
# level = DEBUG => you can print debug messages + message types that are below debug (info,warning, error, critical)
# same rule for each other level
# if you are specifying an file name then logs are not printed to console anymore
# default file mode is append
logging.basicConfig(level=logging.DEBUG, filename='output.log', filemode="w")

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')