n = input('Escreva um inteiro positivo:\n ? ')
i=len(n)-1
numero=0

while i >= 0 :
    numero=numero*10 + int(n[i])
    i-=1
print(numero)