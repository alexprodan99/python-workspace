import logging
user_data = {
    'username' : 'aprodan'
}
fmtstr = 'User: %(username)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s'
datestr = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(filename="output.log", level=logging.DEBUG, filemode="w", format=fmtstr, datefmt=datestr)

# you can add optional extra data too
logging.debug('Debug message', extra=user_data)
logging.info('Info message', extra=user_data)
logging.warning('Warning message', extra=user_data)
logging.error('Error message', extra=user_data)
logging.critical('Critical message', extra=user_data)