#!usr/bin/env python
"""Imprime as tabuadas de 1 à 10"""
__version__ = "0.1.1"
__author__ = "Lucas Matsuse"

base = list(range(1,11))
template = """
---tabuada do {numero} ---

         {operacao}         

###################
"""

for i in base:
    texto = f"Tabuada do {i}"
    cabecalho = "{:-^20}".format(texto)
    print(cabecalho)
    print()
    for j in base:
        operacao = f"{i} X {j} = {i*j}"
        print("{:-^20}".format(operacao))
    print()
    print(20*"#")
