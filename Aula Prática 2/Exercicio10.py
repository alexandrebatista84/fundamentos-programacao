n = input('Escreva um inteiro positivo: ')
i=0
number=0
while i < len(n):
    if (int(n[i]) % 2) != 0:
        number=number*10+int(n[i])    
    i+=1
print(number)
