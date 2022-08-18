import random
from string import Template

import pokemon
from pokemon import tipo_pokemon

import get_module
import relaciones
from relaciones import relaciones_2
from species import tipo_especial, textos
traduccion = {'normal': 'Normal', 'fighting': 'Lucha', 'flying': 'Volador', 'poison': 'Veneno', 'ground': 'Tierra', 'rock': 'Roca', 'bug': 'Bicho', 'ghost': 'Fantasma', 'steel': 'Acero', 'fire': 'Fuego', 'water': 'Agua', 'grass': 'Planta', 'electric': 'Eléctrico', 'psychic': 'Psíquico', 'ice': 'Hielo', 'dragon': 'Dragón', 'dark': 'Siniestro', 'fairy': 'Hada', 'unknown': '???', 'shadow': None, 'baby' : 'Bebé', 'legendary': 'Legendario', 'mythical': 'Mítico'}

def template_html(nombre_pokemon):
    pokemon_name = nombre_pokemon
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    dict_pokemon = get_module.get_info(url)
    pokemon_id = dict_pokemon.get('id')
    stats_pokemon = pokemon.stats_pokemon(dict_pokemon)

    url2 = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}'
    dict_species = get_module.get_info(url2)
    if dict_species.get('evolves_from_species'):
        etapa_previa = f"Etapa Previa: {dict_species.get('evolves_from_species').get('name').capitalize()}"
    else:
        etapa_previa = ''

    pokemon_tipo_especial = tipo_especial(dict_species)
    pokemon_tipos_base = tipo_pokemon(dict_pokemon)
    pokemon_tipos_total = pokemon_tipo_especial + pokemon_tipos_base
    tipos_total = ''
    for tipo in pokemon_tipos_total:
        tipos_total += Template('''<span class="label $tipo">$tipo2</span>''').substitute(tipo=tipo,
                                                                                          tipo2=traduccion.get(tipo))

    lista_diccionarios_tipos_base = []
    for tipo in pokemon_tipos_base:
        url3 = f'https://pokeapi.co/api/v2/type/{tipo}/'
        lista_diccionarios_tipos_base.append(get_module.get_info(url3))

    pokemon_relaciones = relaciones_2(lista_diccionarios_tipos_base)

    imagen = dict_pokemon.get('sprites').get('other').get('official-artwork').get('front_default')
    texto = random.choice(textos(dict_species))

    super_efectivo = relaciones.super_efectivo(pokemon_relaciones)
    debil_contra = relaciones.debil_contra(pokemon_relaciones)
    resistente_contra = relaciones.resistente_contra(pokemon_relaciones)
    poco_eficaz = relaciones.poco_eficaz(pokemon_relaciones)
    inmune = relaciones.inmune(pokemon_relaciones)
    ineficaz = relaciones.ineficaz(pokemon_relaciones)

    if pokemon_name == 'type-null':
        pokemon_name = 'código cero'

    html = Template('''<!DOCTYPE html>
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="mystyle.css">
            <title>$name</title>
        </head>
    <body>

        <div class="column2">
        <div class="card">
        <h1>#$id $name</h1>
            <img src=$imagen width="150" height="150">
        <div class="container">
            <h4>$etapa_previa</h4>
            <h2>Estadísticas</h2>
            <table>
                <tr>
                   <td><h5>HP: $hp</h5></td>
    <td><h5>Ataque: $ataque</h5></td>
    <td><h5>Defensa: $defensa</h5></td>
    <td><h5>Ataque Especial: $aspecial</h5></td>
    <td><h5>Defensa Especial: $dspecial</h5></td>
    <td><h5>Velocidad: $velocidad</h5></td>
                </tr>
            </table>
            <h3><b>Tipo</b></h3>
                $tipos
            <p>$texto</p>

        <h3>Super efectivo contra:</h3>
            $super_efectivo
        <h3>Débil contra:</h3>
            $debil_contra
        <h3>Resistente contra:</h3>
            $resistente_contra
        <h3>Poco Eficaz contra</h3>
            $poco_eficaz
        <h3>Inmune contra:</h3>
            $inmune
        <h3>Ineficaz contra:</h3>
            $ineficaz

        </div>
        </div>

    </body>
    </html>''').substitute(id=pokemon_id, name=pokemon_name.replace('-', ' ').title(), imagen=imagen, etapa_previa= etapa_previa,hp=stats_pokemon.get('hp'),
                           ataque=
                           stats_pokemon.get('attack'), defensa=stats_pokemon.get('defense'),
                           aspecial=stats_pokemon.get('special-attack'),
                           dspecial=stats_pokemon.get('special-defense'), velocidad=stats_pokemon.get('speed'),
                           tipos=tipos_total,
                           texto=texto, super_efectivo=super_efectivo, debil_contra=debil_contra,
                           resistente_contra=resistente_contra,
                           poco_eficaz=poco_eficaz, inmune=inmune, ineficaz=ineficaz)
    return html



