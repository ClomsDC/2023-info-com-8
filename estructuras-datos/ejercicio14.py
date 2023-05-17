# Crear una tupla con los números del 1 al 5
tupla = (1, 2 ,3 ,4 ,5)
# mostrar la suma de todos los elementos de la tupla
def sumar(numero):
    suma = 0
    for x in numero:
        suma += x
    return suma

print('La suma de los elementos de la tupla es: ', sumar(tupla))
print('\nLa tupla es: ', tupla)