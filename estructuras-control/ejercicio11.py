# Escribir un programa que pida al usuario dos números
numeros = input('Ingrese dos números: ')

a, b= numeros.split(',')
suma= int(a) + int(b)

# la suma de ellos solo si ambos son pares
if a == b:
    print(suma)
else:
    print('Los números no son pares.')