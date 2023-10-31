#!/usr/bin/env python
"""Hello World multi línguas

Este programa exibe a mensagem 'hello, world' na língua em que o ambiente de
execução está configurado.

Como usar:

Confira se a variável LANG está devidamente configura, acessando o ambiente de
execução:

    SET LANG=pt_BR
    ou
    export LANG=pt_BR
ou informe atraves do CLI argument '--LANG=pt_BR'. Caso contrário o programa
pedirá para o usuário informar com o input.
Execução:

    python hello2.py
    ou
    ./hello2.py
"""
__version__ = "0.1.3"
__author__ = "Lucas Matsuse"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang":None,
    "count":1
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        #TODO: logging
        print(f"[Error] {str(e)}")
        print('You need to use "="')
        print('Try with --key=value')
        sys.exit(1)
    key = key.lstrip('-').strip().lower()
    value = value.strip()
    if key not in arguments.keys():
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments['lang']
if arguments['lang'] is None: 
    current_lang = os.getenv("LANG")
    if current_language is None:
        current_language = input(
            "Choose a language "
        )
current_language = current_language[:5]
"""
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
"""
msg ={
    "pt_BR":"Olá, Mundo!",
    "en_US":"Hello, World!",
    "it_IT":"Ciao, Mondo!",
    "fr_FR":"Bonjour Monde!",
    "es_SP":"Hola, Mundo!"
}
try:
    message = msg[current_language]
except KeyError as e:
    print(f'[Error] {str(e)}')
    print(f'Language is invalid, choose from {list(msg.keys())}')
    sys.exit(1)

print( message * int(arguments['count']))