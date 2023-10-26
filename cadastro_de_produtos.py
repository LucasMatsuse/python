#!/usr/bin/env python
"""Cadastro de produtos"""
__version__ = "0.1.0"

produto = {
	"nome": "Caneta",
	"cores": ["azul","branco"],
	"preco": 3.23,
	"dimensao":{
                "altura": 12.1,
	            "largura":  0.8
    },
	"em_estoque": True,
	"codigo": 45678,
	"codebar": None,
}

cliente = {
    "nome":"Lucas",
    "compra":produto,
    "quantidade":3,
}

total_compra=cliente["quantidade"]*cliente["compra"]["preco"]

print(
    f'O cliente {cliente['nome']} comprou {cliente['quantidade']} unidades'
    f' de {cliente['compra']['nome']} e pagou um total de {total_compra}.'
    )