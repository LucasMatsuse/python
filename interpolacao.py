#!usr/bin/env python

import os
import sys
arguments = sys.argv[1:]
if not arguments:
    print('É necesssário passsar os arquivos de emails e de template.')
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path,filename)
templatepath = os.path.join(path,templatename)

for line in open(filepath, encoding='utf-8'):
    nome, email = line.split(',')
    print(f'email enviado para {email}.')
    print()
    print(
        open(templatepath).read()%{
            "nome":nome,
            "produto":"caneta",
            "texto":"Escrever lindos textos",
            "link":"https://canetaslegais.com",
            "quantidade":1,
            "preco":10.0
        }
    )
    print('*'*50)