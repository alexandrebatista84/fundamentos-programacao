def digitos(n):
    if (not isinstance(n, int)) or (n <= 0):
        raise ValueError ('int2digitos: argumento invalido')
    res = ()
    while n != 0:
        res = (n % 10, ) + res
        n = n // 10
    return res

def acumulador(f, lst):
    res = lst[0]
    for x in lst[1:]:
        res = f(res, x)
    return res

def filtra(p, lst):
    res = []
    for x in lst:
        if p(x):
            res.append(x)
    return res

def sem_pares(n):
    return acumulador(lambda x,y: 10*x + y, filtra(lambda x : x%2, digitos(n)))

def soma_divisores(n,total=0,i=1):
    if i>n:
        return total
    else:
        if n%i==0:
            return soma_divisores(n,total+i,i+1)
        else:
            return soma_divisores(n,total,i+1)

print(soma_divisores(10))