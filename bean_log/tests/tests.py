import sys
import time

path = '../BeanLogger'
sys.path.append(path)

import BeanLogger as bl

# send bad logs
my_logger = bl.BeanLogger(url='http://127.0.0.1/Bean', log='test')
my_logger.debug('I am a backlogged debug: {}'.format(time.time()))
my_logger.info('I am a backloggged info: {}'.format(time.time()))
my_logger.warning('I am a backlogged warning: {}'.format(time.time()))
my_logger.error('I am a backlogged error: {}'.format(time.time()))
my_logger.critical('I am a backlogged critical: {}'.format(time.time()))

# connect to the proper log server
my_new_logger = bl.BeanLogger(url='http://192.168.0.3:8280/Bean', log='test')
my_new_logger.debug('I am a debug: {}'.format(time.time()))
my_new_logger.info('I am an info: {}'.format(time.time()))
my_new_logger.warning('I am a warning: {}'.format(time.time()))
my_new_logger.error('I am an error: {}'.format(time.time()))
my_new_logger.critical('I am a critical: {}'.format(time.time()))

# retreive logs
