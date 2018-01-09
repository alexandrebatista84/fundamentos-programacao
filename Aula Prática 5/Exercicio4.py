def soma_cumulativa(lista):
    for i in range(1,len(lista)):
        lista[i]=lista[i]+lista[i-1]
    return lista

print(soma_cumulativa([1,2,3,4,5]))