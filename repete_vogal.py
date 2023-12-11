#!/usr/bin/env python3
#teste = True
palavras = []
while True:
#while teste:
    palavra = input('Digite um palavra (ou Enter para sair) ').strip()
    palavranova = ''
    for letra in palavra:
        palavranova += letra
        #TODO: remover acentuação usando funções
        if letra.lower() in 'aeiouáàãâéêíóôõú':
            palavranova += letra
        #palavranova += letra*2 if letra.lower() in 'aeiouáàãâéêíóôõú' else letra
    palavras.append(palavranova)
    if not palavra:
        break
    #if palavranova == '':
        #teste = False

print(*palavras, sep='\n')