#!usr/bin/env python3
'''Bloco de notas simples

py notes.py new "minhas anotações"
tag:'tag'
texto:
'escreva qualquer texto de uma linha aqui.'

py  notas.py read --tag=tech
...
...
...
...

'''

import os
import sys

path = os.curdir
filepath = os.path.join(path,'notes.txt')

arguments = sys.argv[1:]
cmd = ['new','read']
if not arguments:
    print(f'Enter a valid command: {cmd}')
    sys.exit(1)

if arguments[0] not in cmd:
    print(f'Invalid command: {arguments[0]}')
    sys.exit(1)

if arguments[0] == 'new':
    tag = input('tag: ')
    texto = input('texto: ')
    with open(filepath,'a') as file_:
        file_.write(f'{arguments[1]}\n')
        file_.write(f'tag: {tag}\n')
        file_.write(f'texto:\n{texto}\n')
        file_.write(50*'-')
        file_.write('\n')
if arguments[0] == 'read':
    if len(arguments)<2:
        print('enter the text tag.')
        sys.exit(1)
    tag = arguments[1].split('=')
    
    with open(filepath) as file_:
        for line in file_:
            if tag[1] in line:
                print(file_.read())