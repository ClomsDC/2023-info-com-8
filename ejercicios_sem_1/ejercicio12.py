nacimiento= input("Colocar su fecha de nacimiento en formato \"dd/mm/aaaa\": ")
fecha= input("Colocar fecha actual en formato \"dd/mm/aaaa\": ")

l1= nacimiento.split("/")
l2= fecha.split("/")

print(f"El usuario tiene aprox. {int(l2[2]) - int(l1[2])} años")