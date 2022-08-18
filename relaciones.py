import json
from string import Template

import requests as requests
traduccion = {'normal': 'Normal', 'fighting': 'Lucha', 'flying': 'Volador', 'poison': 'Veneno', 'ground': 'Tierra', 'rock': 'Roca', 'bug': 'Bicho', 'ghost': 'Fantasma', 'steel': 'Acero', 'fire': 'Fuego', 'water': 'Agua', 'grass': 'Planta', 'electric': 'Eléctrico', 'psychic': 'Psíquico', 'ice': 'Hielo', 'dragon': 'Dragón', 'dark': 'Siniestro', 'fairy': 'Hada', 'unknown': '???', 'shadow': None}

def relaciones(diccionario):
    relaciones = {}
    for key in diccionario.get('damage_relations').keys():
        lista = []
        for item in diccionario.get('damage_relations').get(key):
            lista.append(item.get('name'))
        relaciones[key] = lista
    return relaciones

def relaciones_2(diccionarios):
    relaciones = {}
    for diccionario in diccionarios:
        for key in diccionario.get('damage_relations').keys():
            lista = []
            for diccionario in diccionarios:
                for item in diccionario.get('damage_relations').get(key):
                        if item.get('name'):
                            lista.append(item.get('name'))
                            lista_sin_duplicados = list(dict.fromkeys(lista))
                            relaciones[key] = lista_sin_duplicados
    return relaciones

def super_efectivo(relaciones):
    super_efectivo = ''
    if relaciones.get('double_damage_to'):
        for item in relaciones.get('double_damage_to'):
            super_efectivo +=Template('''<span class="label $item">$item2</span>''').substitute(item=item, item2=traduccion.get(item))
    return super_efectivo

def debil_contra(relaciones):
    debil_contra = ''
    if relaciones.get('double_damage_from'):
        for item in relaciones.get('double_damage_from'):
            debil_contra +=Template('''<span class="label $item">$item2</span>''').substitute(item=item, item2=traduccion.get(item))
    return debil_contra

def resistente_contra(relaciones):
    resistente_contra = ''
    if relaciones.get('half_damage_from'):
        for item in relaciones.get('half_damage_from'):
            resistente_contra += Template('''<span class="label $item">$item2</span>''').substitute(item=item,
                                                                                           item2=traduccion.get(item))
    return resistente_contra

def poco_eficaz(relaciones):
    poco_eficaz = ''
    if relaciones.get('half_damage_to'):
        for item in relaciones.get('half_damage_to'):
            poco_eficaz += Template('''<span class="label $item">$item2</span>''').substitute(item=item,
                                                                                                item2=traduccion.get(item))
    return poco_eficaz

def inmune(relaciones):
    inmune = ''
    if relaciones.get('no_damage_from'):
        for item in relaciones.get('no_damage_from'):
            inmune += Template('''<span class="label $item">$item2</span>''').substitute(item=item, item2=traduccion.get(item))
    return inmune

def ineficaz(relaciones):
    ineficaz = ''
    if relaciones.get('no_damage_to'):
        for item in relaciones.get('no_damage_to'):
            ineficaz += Template('''<span class="label $item">$item2</span>''').substitute(item=item, item2=traduccion.get(item))
    return ineficaz

def tipo_espanol(diccionario):
    for item in diccionario.get('names'):
        if item.get('language').get('name') == 'es':
            espanol = item.get('name')
            return espanol

if __name__ == '__main__':
    names = {}
    poder = 'ice'
    poder2 = 'flying'
    url3 = f'https://pokeapi.co/api/v2/type/{poder}/'
    url4 = f'https://pokeapi.co/api/v2/type/{poder2}/'

    response3 = requests.request('GET', url3)
    response4 = requests.request('GET', url4)
    tipo_dict = json.loads(response3.text)
    tipo2_dict = json.loads(response4.text)




    danos = relaciones(tipo_dict)
    danos2 = relaciones(tipo2_dict)
    print(danos)
    print(danos2)
    rela2 = relaciones_2([tipo_dict, tipo2_dict])
    print(rela2)

    url5 = 'https://pokeapi.co/api/v2/type/'
    response5 = requests.request('GET', url5)
    tipos_dict = json.loads(response5.text)

    lista_tipos_ingles = []
    for item in tipos_dict.get('results'):
        lista_tipos_ingles.append(item.get('name'))
    print(lista_tipos_ingles)


    ingles_espanol = {}
    for item in lista_tipos_ingles:
        url6 = 'https://pokeapi.co/api/v2/type/' + item
        response6 = requests.request('GET', url6)
        diccionario_tipo = json.loads(response6.text)
        ingles_espanol[item] = tipo_espanol(diccionario_tipo)
    print(ingles_espanol)

