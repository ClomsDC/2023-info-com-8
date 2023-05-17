# Escribe un programa que pida al usuario un número
numero = int(input('Ingrese un numero natural: '))

# calcule la suma de todos los números naturales del 1 hasta el número.
suma = 0
for i in range(1, numero + 1):
    suma += i # se va sumando el siguiente valor de i que se encuentre en la lista range
    print(f'{i}, {suma}')
print('La suma de todos los números naturales es =', suma)