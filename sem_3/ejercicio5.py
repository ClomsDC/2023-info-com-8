# Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

suma = 0
for num in range(1,101):
    if num%2 == 0:
        suma += num
print('La suma de los números pares hasta el 100 es de:', suma)
        