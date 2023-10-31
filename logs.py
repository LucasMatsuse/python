#!/usr/bin/env python3
"""Level menor-->maior
notset
debug
info
warning
error
critical
"""
import logging
import os
try:
    1/0
except ZeroDivisionError as e:
    logging.error('%s',str(e))


from logging import handlers
#boilerplate
#TODO: usar função
#TODO: usar lib

log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger('nome',log_level)
#ch = logging.StreamHandler()
#ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    'meulog.log',
    maxBytes =10**6,
    backupCount = 10 
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)