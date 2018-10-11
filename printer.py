from escpos.printer import Usb
from PIL import *
import requests, json
import time

printer = Usb(0x0416, 0x5011)
while True:
    r = requests.get('http://127.0.0.1:8080/api/print/')
    if r.status_code == 200:
        for visitante in r.json():
            print(visitante)
            printer.text('\n\n')
            printer.image('head.gif')
            printer.text('Nome: {}\n'.format(visitante['nome'][0:20]))
            printer.text('Telefone: {}\n'.format(visitante['telefone']))
            printer.text('CPF: {}.xxx.xxx.xxx-xx \n'.format(visitante['documento'][0:3]))
            if visitante['tipo'] == 1:
                printer.text('------------------------------\n')
                printer.text('-----------LOJISTA------------\n')
                printer.text('------------------------------\n')
            printer.image('footer.gif')
            printer.text('------------------------------\n')
            printer.text('\n\n')
            rput = requests.put('http://127.0.0.1:8080/api/print/{}/'.format(visitante['id']),
                    data=json.dumps({'impresso': True}),
                    headers={'Content-Type': 'application/json'})
            print(rput.text)
    time.sleep(3)
    print('loop')
