def soma_quadrados_impares(lista):
    return acumula(lambda x,y: x+y, transforma(lambda x: x**2, filtra(lambda x: x%2!=0,lista)))

def filtra(tst,lst):
    if lst==[]:
        return lst
    else:
        if tst(lst[0]):
            return [lst[0]] + filtra(tst,lst[1:])
        else:
            return filtra(tst,lst[1:])

def transforma(fn,lst):
    if lst==[]:
        return lst
    else:
        return [fn(lst[0])] + transforma(fn,lst[1:])


def acumula(fn,lst):
    if lst==[]:
        return 0
    else:
        return fn(lst[0], acumula(fn,lst[1:]))

print(soma_quadrados_impares([1, 2, 3, 4, 5, 6]))