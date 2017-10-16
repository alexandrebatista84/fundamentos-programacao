n=input('Escreva um número\n-> ')

i=len(n)-1
inv=0

while i >= 0 :
    inv=inv*10 + int(n[i])
    i-=1

i=len(n)
n=int(n)

while i > 0:
    n = n*10
    i-=1

print(n+inv)