nota= int(input('Ingrese su nota del 0-10: '))

if nota<=10 and nota>=5:
    print(f'\n¡Felicidades! Ha aprovado con una nota de {nota} puntos.\n')
elif nota>=0 and nota<5:
    print(f'\nSu nota a sido de {nota} puntos. No ha alcanzado ¡Siga practicando!\n')
else:
    print(f'\nNo ha ingresado una nota valida.\n')