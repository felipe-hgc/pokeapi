
import webbrowser
import os
import time

import poke_validation
from crea_html import template_html

def show_pics(html, nombre):
    with open(f'{nombre}.html','w') as f:
        f.write(html)
    print('Las fotos se mostrarán en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')

pokemon_name=poke_validation.validate(input("Ingrese el nombre de un pokemon: ").replace(' ', '-').lower())
html = template_html(pokemon_name)
show_pics(html,'temporal')



