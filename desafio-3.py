# importar de la biblioteca random la función randint
from random import randint

intentos = 8
intento = 0
num_random = randint(1, 100) #genera un numero random entre 1-100

# Pedir al usuario que ingrese su nombre.
nombre = input('Ingrese su nombre: ')

print('\nHay un número escondido entre el 1 y 100.')
print(f'Tiene 8 intentos para adivinarlo.')

# Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
while intentos > 0:
    num = input('\nIngrese un número: ')
    num_ent = num.isdigit()

    if num_ent == False: # Si el numero ingresado es decimal
        print(f'\nEl número ingresado no es valido. Intentalo de nuevo.')
        num = input('Ingrese un número: ')
        # muestra las pistas del nuevo intento
        if int(num) < num_random: 
            print('\nEl número escondido es mayor al ingresado.')
        elif int(num) > num_random:
            print('\nEl número escondido es menor al ingresado.')
        else:
            print(f'''
¡Felicidades {nombre}! Adivinaste el número escondido.
    Lo encontraste en el intento {intentos}.
    ''')
            break # Si adivina el número corta el programa.

    elif int(num) < num_random: # Si el número es mayor
        print('\nEl número escondido es mayor al ingresado.')
    elif int(num) > num_random: # Si el número es menor
        print('\nEl número escondido es menor al ingresado.')
    else: # Si el usuario adivina el número.
        print(f'''
¡Felicidades {nombre}! Adivinaste el número escondido.
    Lo encontraste en el {intento}° intento.
    ''')
        break # si lo adivina corta el programa
        
    intentos -= 1
    intento += 1
    print(f'Tienes {intentos} intentos.')
    
    if intento == 8: # Al quedarse sin intentos imprime el print.
        print(f'''
---------- |Fallaste| ----------
   No lograste encontrar en número. 
   El número escondido era: {num_random}
   ¡Suerte para la proxima {nombre}!
''')