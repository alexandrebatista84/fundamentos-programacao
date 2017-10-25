def elemento_matriz(matriz,l,c):

    
    if (l>=len(matriz)):
        return "Índice inválido: linha ",l

    a=matriz[l]

    return a[c]

print(elemento_matriz([[1, 2, 3],[4, 5, 6]],2,2))