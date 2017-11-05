def elemento_matriz(matriz,l,c):

    if (l>=len(matriz)):
        print('Índice inválido: linha ',l)
    if (c>=len(matriz[0])):
        print('Índice inválido: coluna ',c)
    else:
        return matriz[l][c]


a=[[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]]
print(elemento_matriz(a,0,6))