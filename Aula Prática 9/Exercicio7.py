# a)
def escreve_esparsa(matrix):
    tam=(0,0)
    for i in matrix:
        if tam[0]<i[0]:
            tam=(i[0],tam[1])
        if tam[1]<i[1]:
            tam=(tam[0],i[1])

    for x in range (tam[0]+1):
        for y in range (tam[1]+1):
            
            if (x,y) in matrix:
                print(matrix[(x,y)],end=' ')
            else:
                print(0,end=' ')
        print()

# b)

def soma_esparsa(e1,e2):

    for x in range (0,len(e1)):
        if x in e2:
            e1[x]=e1[x]+e2[x]
    
    for x in range (0,len(e2)):
        if x not in e1:
            e1[x]=e2[x]

    return e1

e1 = {(1,5): 4, (2, 3): 9, (4, 1): 1}
e2 = {(1, 6): 2, (4, 1): 2, (5,4): 2}
        
escreve_esparsa(soma_esparsa(e1, e2))