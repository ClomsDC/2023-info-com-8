# Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula
texto = input('Ingrese un texto: ')

final = '' # Texto vocio
for x in texto: # en lugar de utilizar la variable 'texto' se usa 'x'
    if x in ('a', 'e', 'i', 'o', 'u'): # Si el texto contiene alguna de estas vocales:
        x = x.upper() # Las transforma en mayuscula.
        final += x # Al texto vacio se le agregan las vocales transformadas en mayuscula.
    else:
        final += x
print(final) # Imprime el texto final modificado.