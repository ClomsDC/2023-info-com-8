numero= int(input('Ingrese un número entero: '))

if numero%2 == 0 and numero%3 == 0:
    print(f'\nEl número {numero} es multiplo de 2 y 3.')
elif numero%2 == 0 and numero%3 != 0:
    print(f'El número es multiplo de 2. No es multiplo de 3.')
elif numero%3 == 0 and numero%2 != 0:
    print(f'El número es multiplo de 3. No es multiplo de 2.')
else:
    print(f'\nEl número {numero} no es multiplo de 2 y 3.')