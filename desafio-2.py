texto = input('Ingrese un texto: ').lower() # pasa el texto original a minúscula.

letra1 = input('Ingrese la primera letra: ')
letra2= input('Ingrese la segunda letra: ')
letra3= input('Ingrese la tercera letra: ')

# Punto 1:
# Cantidad de veces que aparece cada una de letras.
letras= [letra1.lower(), letra2.lower(), letra3.lower()] # pasa las letras a minúscula.

print()
for letra in letras: # pasa por todos los elementos de la lista.
    if len(letra) != 1:
        print('\"Se ha ingresado más de una letra. No se ha podido ejecutar.\"')
    else:
        print(f'La letra \"{letra}\" aparece {texto.count(letra)} en el texto.')

# Punto 2:
# Cuantas palabras hay en total en todo el texto.
palabras = texto.replace(',', ' ') # si el texto tiene una , lo replaza con un espacio
palabras = palabras.replace('.', ' ')
palabras = palabras.replace(':', ' ')
palabras = palabras.replace(';', ' ')
palabras = palabras.replace('?', ' ')
palabras = palabras.replace('!', ' ')
pal = texto.split(' ') # separa las palabras quitando los espacios

cant_pal = len(pal)
if cant_pal == 1:
    print(f'\nEn el texto hay 1 palabra')
else:
    print(f'\nEn el texto hay un total de {cant_pal} palabras')

# Punto 3:
# Cual es la primera letra y cuál es la última.
print(f'\nLa primer letra del texto es: {texto[0]} \nLa ultima letra es: {texto[-1]}')

#Punto 4:
# Mostrar el texto en orden inverso
txt_rev = texto[::-1]
pal_rev = pal[::-1] # invierte el orden de los objetos de la lista
txt_pal_rev = ' '.join(pal_rev) # coloca un espacio entre los elementos de la lista
print('\nTexto invertido: ', txt_pal_rev)
print('Palabras invertidas: ', txt_rev)

#Punto 5:
# Decir si la palabra "python" aparece en el texto.
aparece = 'python' in texto # usa bool para verificar si se encuentra
opciones = {True: 'aparece', False: 'no aparece'}
print('\nLa palabra \"Python\"', opciones[aparece], 'en el texto \2')