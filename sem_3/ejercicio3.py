# Escribe un programa que pida al usuario un número
numero = int(input('Ingrese un número: '))

# imprima la tabla de multiplicar correspondiente a ese número del 1 al 10.

for num in range(1,11):
    multiplicacion = numero * num
    print(numero, '*', num, '=', multiplicacion)
