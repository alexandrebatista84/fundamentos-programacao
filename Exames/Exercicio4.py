def cria_multiplos(n):

    if ((not isinstance(n,int)) | (n<=0)):
        raise ValueError("Argumento Inválido")
    
    l=[]

    for i in range(10):
        l.append(i*n)

    return l

print(cria_multiplos(1))