# -Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio.

numeros = input('Ingrese numeros separados con comas: ')

numeros = numeros.replace(' ', ',')
numero = numeros.split(',')

while '' in numero:
    numero.remove('')
num = [int(x) for x in numero]

suma = sum(num)

print(f'El promedio de {num} es: ', suma // len(num))