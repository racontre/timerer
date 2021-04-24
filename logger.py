"""
https://blog.miguelgrinberg.com/post/the-ultimate-guide-to-python-decorators-part-iii-decorators-with-arguments
21.04.2021
todo: make logger take args
"""
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def __init__(self):       
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')
    self.logger = logging.getLogger('main')
        
def log(func):
    def inner(*args, **kwargs):
        logging.info('Called a function')
        result = func(*args, **kwargs)
        return result
    return inner