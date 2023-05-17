# Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número

numero = int(input('Ingrese un numero: '))

fib = [0, 1]
while True:
    suma_ant = fib[-2] + fib[-1]
    if (suma_ant > numero):
        print(f'''
La secuencia Fibonacci es mayor al número {numero}.
El número anterior de la secuencia es: {fib[-1]}
        ''')
        break
    elif (suma_ant == numero):
        print(f'''
La secuencia Fibonacci correspondiente al número es: {fib}
        ''')
        break
    else:
        fib.append(suma_ant)