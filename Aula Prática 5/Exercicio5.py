def elemento_matriz(matriz,l,c):

    if (l>=len(matriz)):
        print("Indice invalido: linha",l)
    if (c>=len(matriz[0])):
        print("Indice invalido: coluna",c)
    else:
        return matriz[l][c]


a=[[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]]
elemento_matriz(a,6,6)