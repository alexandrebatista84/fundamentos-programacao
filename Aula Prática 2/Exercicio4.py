x=eval(input("Escreva um número em segundos: "))
dias=0;
horas=0;
minutos=0;
segundos=0;
dias = x//3600//24
horas = x//3600 - dias*24 
minutos = x//60 - horas*60 - dias*24*60
segundos = x - dias*24*3600 - horas*3600 - minutos*60 
print("Dias:", dias,"   Horas:", horas,"   Minutos:", minutos,"   \
Segundos:", segundos)


            