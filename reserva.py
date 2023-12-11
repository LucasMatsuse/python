import os
import sys
import logging

path = os.curdir
filepath = os.path.join(path,'reservas.txt')

quartos = {}
reserva = {}

try: 
    for line in open('quartos.txt'):
        cod, nome, preco = line.strip().split(',')
        quartos[int(cod)] = {
            'nome':nome,
            'preço':float(preco),  #TODO: Decimal
            'disponivel':True
        }
    for line in open('reservas.txt'):
        cod, cliente, dias = line.strip().split(',')
        reserva[int(cod)] = {
            'cliente':cliente,
            'dias':int(dias)
        }
except FileNotFoundError:
    logging.error('O arquivo com os quartos/reservas não existe.')
    sys.exit(1)


for i in reserva.keys():
    if i in quartos.keys():
        quartos[i]['disponivel'] = False


print('Nossos quartos disponíveis são')
for codigo, dados in quartos.items():
    nome = dados['nome']
    preco = dados['preço']
    disp = dados['disponivel']
    if disp:
        print(f'{codigo} - {nome} - R$ {preco}')

try:
    cliente = input('Informe seu nome: ').strip().capitalize()
    quarto = int(input('Informe o código do quarto: ').strip())
    if not quartos[quarto]['disponivel']:
        print('O quarto informado está ocupado.')
        sys.exit(1)
    if quarto == 0 or quarto > len(quartos.keys()):
        print('O quartos informado não existe.')
        sys.exit(1)
    dias = int(input('Informe quantos dias irá ficar: ').strip())
    with open(filepath,'a') as file_:
        file_.write(f'{quarto},{cliente},{dias}')
        file_.write('\n')
except ValueError:
    logging.error('Informe um número para quantos dias irá ficar e para o código do quarto')
    sys.exit(1)

print(f'Obrigado(a) por se hospedar conosco {cliente}, você reservou o quarto {quarto}'
    f' por {dias} dias, o valor da sua hospedagem sem os custos adicionais de consumo'
    f' será de {dias*quartos[quarto]['preço']} reais')