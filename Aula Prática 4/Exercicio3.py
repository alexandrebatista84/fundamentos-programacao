def implode (t): 
    i=0
    resultado=0
    length = len(t)
    while i < length:
        if not isinstance(t[i],int):
            raise ValueError ('implode: elemento não inteiro')
        resultado = resultado*10 + t[i]
        i = i +1
    return resultado

print(implode((2,'a',2)))

