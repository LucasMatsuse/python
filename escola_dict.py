#!/usr/bin/env python
"""Exibe um relatório de estudantes por atividade.

Imprimir a lista de estudantes agrupados por sala que estão matriculados em 
cada atividade.
"""
__version__ = "0.1.1"

sala1 =["Erik",'Maia',"Gustavo","Manuel","Sofia","Joana"]
sala2 = ["João","Antonio","Carlos","Maria","Isolda","Lucas"]

ingles = ['Erik','Maia','Joana','Carlos','Antonio']
musica = ['Erik','Carlos','Maria']
danca = ['Gustavo','Sofia','Joana','Antonio']

"""
atividades = [("Inglês",ingles), ("Música",musica), ("Dança",danca)]
for aula , atividade in atividades:
    Atividade_sala_um = set(sala1) & set(atividade)
    Atividade_sala_dois = set(sala2) & set(atividade)

    """"""for aluno in atividade:
        if aluno in sala1:
            Atividade_sala_um.append(aluno)
        elif aluno in sala2:
            Atividade_sala_dois.append(aluno)
    """"""    
    print(f'{aula} - Sala 1: {Atividade_sala_um}')
    print(f'{aula} - Sala 2: {Atividade_sala_dois}')
    print('-'*50)
"""    
atividades = {
    "Inglês":{
        "Sala 1":list(set(sala1) & set(ingles)),
        "Sala 2":list(set(sala2) & set(ingles))
    },
    "Música":{
        "Sala 1":list(set(sala1) & set(musica)),
        "Sala 2":list(set(sala2) & set(musica))
    },
    "Dança":{
        "Sala 1":list(set(sala1) & set(danca)),
        "Sala 2":list(set(sala2) & set(danca))
    }
}
for atividade in atividades.keys():
    print()
    for sala in atividades[atividade].keys():
        print(f'{atividade} - {sala}: {atividades[atividade][sala]}\n')
    print('#'*50)