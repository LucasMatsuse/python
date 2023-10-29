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
__version__ = "0.1.0"

import sys




if len(sys.argv) >= 4:
    func = sys.argv[1].strip('-').lower().strip()
    n1 = float(sys.argv[2].strip('-'))
    n2 = float(sys.argv[3].strip('-'))
else:
    func = input('digte a operação: ')
    n1 = float(input('digite o primeiro número: '))
    n2 = float(input('digite o segundo número: '))


divzero = (func=='div') and (n2==0)
if divzero:
    print('Não é possível fazer divisões por 0.')
    n2 = 1
resultado = {
    'erro': 'Você digitou uma operação que esse programa não resolve, ou'
            ' não passou a operação como primeiro argumento.',
    'sum': n1 + n2,
    'sub': n1 - n2,
    'mul': n1 * n2,
    'div': n1 / n2
}
if func not in resultado.keys():
    func = 'erro'

print(resultado[func])
