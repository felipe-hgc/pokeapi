import json
import requests

def textos(diccionario):
#    lista_espanol = []
#    for flavor in diccionario.get('flavor_text_entries'):
#        if flavor.get('language').get('name') == 'es':
#            lista_espanol.append(flavor.get('flavor_text'))
    lista_espanol = [flavor.get('flavor_text') for flavor in diccionario.get('flavor_text_entries') if flavor.get('language').get('name') == 'es']
    return lista_espanol

def tipo_especial(species_dict):
    tipo = []
    if species_dict.get('is_legendary'):
        tipo = ["legendary"]
    elif species_dict.get('is_baby'):
        tipo = ["baby"]
    elif species_dict.get('is_mythical'):
        tipo = ["mythical"]
    return tipo

if __name__ == '__main__':
    pokemon = 'articuno'
    url2 = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}'
    response2 = requests.request('GET', url2)
    species_dict = json.loads(response2.text)

    print(species_dict.get('is_legendary'))
    print(species_dict.get('is_baby'))
    print(species_dict.get('is_mythical'))

    textos_espanol = textos(species_dict)
    print(textos_espanol)

    prueba_tipo_especial = tipo_especial(species_dict)
    print(prueba_tipo_especial)

