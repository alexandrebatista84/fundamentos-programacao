#def implode (t): 
#    i=0
#    resultado=0
#    length = len(t)
#    while i < length:
#       if not isinstance(t[i],int):
#            raise ValueError ('implode: elemento não inteiro')
#        resultado = resultado*10 + t[i]
#        i = i +1
#    return resultado


def implode (t):
    resultado=0
    for i in t:
        if not isinstance(i,int):
            raise ValueError ('implode: elemento não inteiro')
        resultado = resultado*10 + i
    return resultado  

print(implode((3,4,0,0,4)))