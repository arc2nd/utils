#!/usr/bin/env python

import os
import json
import logging
from logging.handlers import RotatingFileHandler

if os.path.exists('config.json'):
    with open('config.json', 'r') as fp:
        CONFIG = json.load(fp)
else:
    CONFIG = {
                'FORMAT': '%(levelname)s :: %(asctime)s :: %(message)s', 
                'LOG_PATH': '/data'
             }

logging.basicConfig(format=CONFIG['FORMAT'], level=logging.DEBUG)


# without this the logging module will just keep generating new logging
# handlers everytime we run the bean function and you'll get increasing 
# numbers of duplicate logs. This keeps a list of our generated loggers 
# and attempts to reuse them

# ok, actually it's not working right, but there's still hope, so we'll leave it in
LOGGERS = {}

def my_logger(name):
    # print('1: {}'.format(LOGGERS))
    if LOGGERS.get(name):
        return LOGGERS.get(name)
    else:
        # print('creating logger: {}'.format(name))
        logger = logging.getLogger(name)
        # if logger.hasHandlers():
        #     logger.handlers.clear()
        logger.setLevel(logging.DEBUG)
        # fh = logging.FileHandler(name)
        fh = RotatingFileHandler(name, maxBytes=5242880, backupCount=5)
        formatter = logging.Formatter(CONFIG['FORMAT'])
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        LOGGERS[name] = logger
        # print('2: {}'.format(LOGGERS))

        return logger

def bean(log='default', level='debug', hostname=None, ip=None, user=None, msg=None):
    this_log = os.path.join(CONFIG['LOG_PATH'], '{}.log'.format(log))
    logger = my_logger(this_log)

    payload = r'USER: {}, HOST: {}, IP: {}: MSG: {}'.format(user, hostname, ip, msg)
    if 'debug' in level.lower():
        logger.debug(payload)
    if 'info' in level.lower():
        logger.info(payload)
    if 'warning' in level.lower():
        logger.warning(payload)
    if 'error' in level.lower():
        logger.error(payload)
    if 'critical' in level.lower():
        logger.critical(payload)

    del(logger)
