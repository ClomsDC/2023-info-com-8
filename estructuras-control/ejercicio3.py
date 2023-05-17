numeros= input('Ingrese dos números: ')

num, numero = numeros.split(",")

if num > numero:
    print(f'{num} es mayor que {numero}')
else:
    print(f'{numero} es mayor que {num}')