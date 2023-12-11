#!/usr/bin/env python3

import sys
import logging
log = logging.Logger('alerta')

info = {
    'temperatura':None,
    'umidade':None
}
keys = info.keys()
for key in keys:
    try:
        info[key] = float(input(f'informe a {key.capitalize()}: ').strip())
    except ValueError:
        log.error(f'{key.capitalize()} inválida')
        sys.exit(1)

temp = info['temperatura']
umidade = info['umidade']

if temp > 45 :
    print('ALERTA!!! Perigo de calor extremo!')
elif (temp*3) >= umidade:
    print('ALERTA!!! Perigo de calor umido!')
elif 10<=temp<=30:
    print('Temperatura normal.')
elif 0<=temp<10:
    print('Frio.')
else:
    print('ALERTA!!! Frio extremo!')