def lista_codigos(a):
    l=[]
    i=0
    
    while i<len(a):
        l.append(ord(a[i]))
        i+=1
    return l


print(lista_codigos("bom dia"))