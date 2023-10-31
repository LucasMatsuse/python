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

#boilerplate
#TODO: usar função
#TODO: usar lib

log_level = os.getenv("LOG_LEVEL","WARNIG").upper()
log = logging.Logger('nome',log_level)
ch = logging.StreamHandler()
ch.setlevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.SetFormatter(fmt)
log.addHandler(ch)