def maior_inteiro(limite,soma=0,aux=0):
    if soma==limite:
        return aux-1
    elif soma>limite:
        return aux-2
    else:
        return maior_inteiro(limite,soma+aux,aux+1)

print(maior_inteiro(28))