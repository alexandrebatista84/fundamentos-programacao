def conta_menores(tuplo,num):
    count=0
    for i in tuplo:
        if i<num:
            count+=1
    return count

#print(conta_menores((3,4,5,6,7),5))

def soma_divisores(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=i

    return count

def parte(lista,n,menores=[],maiores=[]):

    if lista==[]:
        return [menores,maiores]
    else:
        if lista[0]<n:
            return parte(lista[1:],n,menores+[lista[0]],maiores)
        else:
            return parte(lista[1:],n,menores,maiores+[lista[0]])
    
#print(parte([3, 5, 1, 4, 5, 8, 9], 4))

#print(soma_divisores(20))
#print(soma_divisores(13))

def max_div(n, d):
    while n % d == 0:
        n = n//d
    return n

print(max_div(300,2))

def soma_quadrados_lista(lista):
    return reduce(lambda x,y: x+y,map(quadrado,lista))

print(soma_quadrados_lista([1,2,3,4,5]))