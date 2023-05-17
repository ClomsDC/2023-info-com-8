numeros= input('Ingrese tres números: ')

num, nume, numero= numeros.split(',')

if num > nume and numero:
    print(num, 'Es el mayor entre: ', numeros)
elif nume > num and numero:
    print(nume, 'Es el mayor entre: ', numeros)
else:
    print(numero, 'Es el mayor entre: ', numeros)