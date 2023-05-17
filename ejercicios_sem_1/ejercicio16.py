peso= float(input('Ingresar peso del usuario: '))
altura= float(input('Ingresar altura del usuario: '))

imc= peso / (altura**2)

print(f'''
El indice de masa corporar del usuario es de:
{imc}
''')