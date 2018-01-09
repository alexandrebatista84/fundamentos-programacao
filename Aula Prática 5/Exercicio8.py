def mul_matrix(m1,m2):

    for x in range(0, len(m1)):
        for y in range(0, len(m1[x])):
            m1[x][y]=m1[x][y]*m2[x][y]
    return m1

def escreve_matriz(m):

    for i in m:
        for x in i:
            print(x,end=" ")
        print()


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
escreve_matriz(mul_matrix(m1,m2))