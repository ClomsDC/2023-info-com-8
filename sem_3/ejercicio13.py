# Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****

numero = int(input('Ingrese un número: '))

lista = []
for num in range(1, numero+1):
    lista.append('*')
    piramide = ''.join(lista) # transforma la lista en str
    print(piramide)