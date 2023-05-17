palabra = input('Ingrese una palabra: ')

pal = palabra.split(' ')
pal_rev = palabra[::-1]

if len(pal) > 1:
    print('\nSe a ingresado más de una palabra. Intente de nuevo \2')
elif palabra.isdigit():
    print('\nSe a ingresado un número. Vuelve a intentarlo \2')
elif pal_rev == palabra:
    print(f'\nLa palabra \"{palabra}\" es palíndroma')
else:
    print(f'\nLa palabra \"{palabra}\" no es palíndroma')