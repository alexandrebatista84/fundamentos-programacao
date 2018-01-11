def soma_divisores(n,aux=1,soma=0):
    
    if aux>n:
        return soma
    else:
        if (n%aux==0):
            return soma_divisores(n,aux+1,soma+aux)
        else:
            return soma_divisores(n,aux+1,soma)


print(soma_divisores(8))