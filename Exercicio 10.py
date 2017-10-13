n = input('Escreva um inteiro positivo: ')
i=0
while i < len(n):
    if (int(n[i]) % 2) != 0:
        print(n[i], end='')
    i+=1
    
