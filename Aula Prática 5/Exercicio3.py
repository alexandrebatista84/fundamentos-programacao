def junta_ordenadas(a,b):
    a=a+b
    c=sorted(a)
    #a.sort() também devolve a lista ordenada. esta função apenas funciona em listas
    # a função sorted funciona com qualquer iterável
    return c 

print(junta_ordenadas([2,5,90],[3,5,6,12]))