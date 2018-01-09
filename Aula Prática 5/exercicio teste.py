def potencia(x, k):
    if k < 0:
        raise ValueError('potencia: expoente k negativo')
    elif type(k) != int:
        raise ValueError('potencia: expoente k não inteiro')
    elif type(x) != int and type(x)!= float:
        raise ValueError('potencia: base x nao é um numero')

    resultado = 1
    while k > 0:
        resultado = resultado * x
        k = k - 1
    return resultado

print(potencia('a',1))

