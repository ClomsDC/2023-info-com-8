# pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante

letra= input('Ingrese una letra: ')

vocales = {'a', 'e', 'i', 'o', 'u'}
vocalM = {'A', 'E', 'I', 'O', 'U'}

if letra in vocales:
    print('La letra es una vocal.')
elif letra in vocalM:
    print('La letra es una vocal.')
else:
    print('La letra es una consonante.')