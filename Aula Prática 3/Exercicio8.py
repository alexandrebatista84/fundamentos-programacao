def valor(q,j,n):

    if ((type(q)!= int) | (q<0) | (not ((j>0) & (j<1))) | (type(n)!= int) | (n<0)):
        return ValueError("Argumento Inválido")

    return q*(1+j)**n 


def duplicar (q,j):

    i=1

    while i>0:

        if valor(q,j,i)>=(2*q):
            return i
            break
        else:
            i=i+1

print(duplicar(100, 0.03))
print(valor(100,0.03,24))