# -Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.

numero = int(input('Ingrese un número: '))
print()

factorial = [1]
for num in range(1, numero + 1):
    producto = factorial[-1] * num
    factorial.append(producto)
    print(factorial)
print(f'\nEl factorial de {numero} es: {factorial[-1]} ')
