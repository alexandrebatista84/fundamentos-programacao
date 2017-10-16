n = input('Escreva um inteiro:\n ? ')
soma=0
i=len(n)-1


while i >= 0 :
    soma=soma + int(n[i])
    i-=1

print(soma)
