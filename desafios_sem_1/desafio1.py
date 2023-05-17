#los vendedores cobran comiciones del 6% de sus ventas
#calcula las comiciones con un programa

nombre= input('Ingrese su nombre: ')
ventas= float(input('Ingrese sus ventas del mes: '))

monto_correspondiente= ventas * 6 / 100

print(f'''
Buenas {nombre}, su monto correspondiente por este mes es de:
{monto_correspondiente}
''')

