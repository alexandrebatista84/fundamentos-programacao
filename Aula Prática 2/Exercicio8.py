
dias=0
n=eval(input('Escreva o número de segundos\n(Um número negativo para terminar)\n? '))

while n>=0:
    dias=n/3600/24
    print('O número de dias correspondente é ',dias)
    n=eval(input('Escreva o número de segundos\n(Um número negativo para terminar)\n? '))