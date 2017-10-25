''' def soma_cumulativa(lista):
    l=[lista[0],]
    i=1
    while i < len (lista):
        l.append(lista[i]+lista[i-1])
        i+=1
    return l  '''


def soma_cumulativa(lista):
    for i in range(1,len(lista), 1):
        lista[i]=lista[i]+lista[i-1]
    return lista

print(soma_cumulativa([1,2,3,4,5,6]))