def agrupa_por_chave(lista):
    dic={}
    for i in range(0,len(lista)):
        if lista[i][0] in dic:
            dic[lista[i][0]].append(lista[i][1])
        else:
            dic[lista[i][0]]=[lista[i][1]]
    
    return dic

print(agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)]))