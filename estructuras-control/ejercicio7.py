caracter= input('Escribe un caracter: ')

if caracter.isalpha():
    print('El caracter es es una letra.')
    if caracter.islower():
        print('Está en minuscula.')
    else:
        print('Está en Mayuscula.')
elif caracter.isdigit():
    print('El caracter es un número.')
else:
    print('El caracter es especial.')