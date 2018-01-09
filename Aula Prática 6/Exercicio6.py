def inverte(lista):

    if len(lista)==1:
        return [lista[0]]
    else:
        return inverte(lista[1:])+[lista[0]]
    
print(inverte([3, 4, 7, 9]))
