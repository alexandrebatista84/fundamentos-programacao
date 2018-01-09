import itertools

def comb(c1,c2):

    if ((type(c1)!=str) |(type(c2)!=str)):
        raise ValueError ("Argumentos Inválidos")

    alfabeto=[]

    for i in range(ord(c1),ord(c2)+1):
        alfabeto.append(chr(i))

    lista=[]

    for x in itertools.combinations_with_replacement(alfabeto,3):
        lista.append(x)
    
    return lista 


print(comb('a','c'))