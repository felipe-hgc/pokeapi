import json
import requests

def tipo_pokemon(diccionario):
    lista_tipos = []
    for type in diccionario.get('types'):
        lista_tipos.append(type.get('type').get('name'))
    return lista_tipos

def lista_sprites(diccionario):
    lista_sprites = []
    for sprite in diccionario.get('sprites').values():
        if sprite != None:
            lista_sprites.append(sprite)
    return lista_sprites

def stats_pokemon(diccionario):
    dict_stats = {}
    for stat in diccionario.get('stats'):
        dict_stats[stat.get('stat').get('name')] = stat.get('base_stat')
    return dict_stats

if __name__ == '__main__':
    pokemon = 'charizard'
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

    response = requests.request('GET', url)
    pokemon_dict = json.loads(response.text)
    stats = stats_pokemon(pokemon_dict)
    print(stats)

    imagenes = lista_sprites(pokemon_dict)
    print(imagenes)

    tipos = tipo_pokemon(pokemon_dict)
    print(tipos)
