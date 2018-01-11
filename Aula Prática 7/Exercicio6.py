def muda(fn, num):
    if num < 10:
        return fn(num)
    else:
        nn = fn(num % 10)
        return nn + 10 ** num_digitos(nn) * muda(fn, num // 10)

def num_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + num_digitos(n // 10)

def soma_dois(n):
    return muda(lambda x: x+2,n)

print(soma_dois(457))

print(soma_dois(986))