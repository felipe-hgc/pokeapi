with open("pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()
    
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]


def validate(name, p_l = pokemon_lista, mensaje = "Ingrese un nombre válido: "):
    if name.replace(' ', '-').lower() =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).replace(' ', '-').lower()
    return name

if __name__ == '__main__':
    name = 'cero'
    print(validate(name))
