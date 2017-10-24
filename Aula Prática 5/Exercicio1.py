def lista_codigos(a):
    l=[]
    i=0

    print a.decode('unicode-escape')
    
    while i<len(a):
        l.append(a.decode(a[i]))
        i+=1
    return l


print(lista_codigos("bom dia"))