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

Execução:

    python hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Lucas Matsuse"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5]


if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)