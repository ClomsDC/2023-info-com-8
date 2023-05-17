# Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

numero = int(input('Ingrese un número: '))

for num in range(1, numero+1):
    num = str(num)*num
    num = ' '.join(num)
    print(num)