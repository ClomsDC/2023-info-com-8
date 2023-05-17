edad= int(input('Ingrese su edad: '))

if edad>=18:
    print(f'''
El usuario tiene {edad} años. 
El usuario es mayor de edad.
    ''')
else:
    print(f'''
El usuario tiene {edad} años.
El usuario es actualmente menor de edad.
    ''')