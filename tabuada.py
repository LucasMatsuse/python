#!usr/bin/env python
"""Imprime as tabuadas de 1 à 10"""
__version__ = "0.1.0"
__author__ = "Lucas Matsuse"

base = list(range(1,11))

for i in base:
    print(f"Tabuada do :{i}")
    for j in base:
        print(f"{i} X {j} = {i*j}")
        
    print(30*"-")
    