def reconhece(c):
    if not isinstance(c,str):
        return False
    aux, i = 0, 0
    while i<len(c):
        if c[i]=='b':
            aux=aux+1
            break
        i=i+1
    return (c[:i]==c[i+1:]) and (aux==1)

print(reconhece("aaaabaaa"))