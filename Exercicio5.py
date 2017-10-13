from math import sqrt

i=0
lista=[]
media=0
devp=0

for i in range (5):
        lista.append(input("Introduza um dos 5 numeros: "))
        media=media+int(lista[i])

media=media/5

i=0

for i in range (5):
        devp=devp+(int(lista[i])-media)**2
        
devp=sqrt(devp/4)

print("A média dos numeros introduzidos é igual a ", media," e o desvio padrão é ",devp)
