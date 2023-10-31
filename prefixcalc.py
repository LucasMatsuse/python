#!usr/bin/env python
"""Calculadora prefix
Funcionamento:
[função] [n1] [n1]

Operações:
sum --> +
sub --> -
mul -- *
div --> /

uso:
py prefix.py sum 2 6
8

py prefix.py mul 2 5
10

py prefix.py
operação: sum
n1: 5
n2: 2
7
"""
__version__ = "0.1.1"

import sys
import os
from datetime import datetime
import logging
from logging import handlers

#logconfig
log_level = os.getenv("LOG_LEVEL","WARNING").upper()
log = logging.Logger('prefixcalc',log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    'prefixcalcerror.log',
    maxBytes =10**6,
    backupCount = 10 
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
fh.setFormatter(fmt)
log.addHandler(ch)
log.addHandler(fh)
#-----------------

if len(sys.argv) == 4:
    func = sys.argv[1].strip('-').lower().strip()
    n1 = float(sys.argv[2].strip('-'))
    n2 = float(sys.argv[3].strip('-'))
else:
    print('Você digitou uma quantidade inesperada de argumentos.')
    func = input('digte a operação: ')
    n1 = float(input('digite o primeiro número: '))
    n2 = float(input('digite o segundo número: '))


try:
    resultado = {
        'sum': n1 + n2,
        'sub': n1 - n2,
        'mul': n1 * n2,
        'div': n1 / n2
    }
    print(resultado[func])

except ZeroDivisionError as e:
    log.error('Não é possível fazer divisão por 0. %s',str(e))
    sys.exit(1)

except KeyError as e:
    log.error('A operação indicada não é válida. %s',str(e))
    sys.exit(1)


path = os.curdir
filepath = os.path.join(path,'prefixcalc.log')
timestamp = datetime.now().isoformat()
user = os.getenv('USER','anonymous')

try:
    with open(filepath,'a') as file_:
        file_.write(f'{timestamp} - {user} - {func}, {n1}, {n2} = {resultado[func]}.\n')
except PermissionError as e:
    log.error('%s',str(e))
    sys.exit(1)
