def conta_palavras(texto):
    
    palavras={}
    texto=texto.split(" ")
 
    for i in range (0,len(texto)):
        if texto[i] in palavras:
            palavras[texto[i]]=palavras[texto[i]]+1
        else:
            palavras[texto[i]]=1
    return palavras

def mostra_ordenado(l):
    lista=[]
    for i in l:
        lista = lista + [[i,l[i]]]

    changed = True
    k = 0
    
    while changed:
        changed = False
        for i in range(len(lista) - 1, k, -1):
            if lista[i-1][0] > lista[i][0]:
                lista[i], lista[i-1] = lista[i-1], lista[i]
                changed = True
        k = k + 1
    
    for i in range(0,len(lista)):
        print(lista[i][0],lista[i][1])

cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'
mostra_ordenado((conta_palavras(cc)))


# def bubblesort(l):
#     changed = True
#     k = 0
#     while changed:
#         changed = False
#         for i in range(len(l) - 1, k, -1):
#             print(l,k)
#             if l[i-1] > l[i]:
#                 l[i], l[i-1] = l[i-1], l[i]
#                 changed = True
#         k = k + 1
#     return l 

