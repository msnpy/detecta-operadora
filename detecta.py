import requests
from bs4 import BeautifulSoup
from os import system;system('clear')



while True:
    print('''\033[1;32m
╔═╗╔═╗╔═══╗╔═╗─╔╗╔═══╗╔╗──╔╗
║║╚╝║║║╔═╗║║║╚╗║║║╔═╗║║╚╗╔╝║
║╔╗╔╗║║╚══╗║╔╗╚╝║║╚═╝║╚╗╚╝╔╝
║║║║║║╚══╗║║║╚╗║║║╔══╝─╚╗╔╝─
║║║║║║║╚═╝║║║─║║║║║─────║║──
╚╝╚╝╚╝╚═══╝╚╝─╚═╝╚╝─────╚╝──
\033[m
    
    ''')
    numero = input('Numero: ')

    replace1 = numero.replace('-', '').replace(' ', '').replace('+55', '')

    url = "http://consultaoperadora.com.br/site2015/resposta.php"

    payload = {'tipo': 'consulta',
            'numero': ''}

    payload['numero'] = replace1

    user_agent = {'User-agent': 'Mozilla/5.0'}

    r = requests.post(url, headers = user_agent, data=payload)

    soup = BeautifulSoup(r.text, 'html.parser')

    div = soup.find('div', {'id': 'resultado_num'})

    try:
        print(f'\033[1;32m{div.get_text()}\033[m')

    except:
        print('\033[31mocorreu um error\033[m')

    
    continua = input('continua sim ou nao?: ').lower()

    if 's' in continua:
        system('clear')

        continue


    else:
        break




