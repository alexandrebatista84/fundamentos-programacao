numero=0
d=eval(input('Escreva um digito\n(-1 para para terminar)\n? '))

while d!=-1:
    numero=numero*10+d
    d=eval(input('Escreva digito\n(-1 para para terminar)\n? '))

print('O número é: ', numero)