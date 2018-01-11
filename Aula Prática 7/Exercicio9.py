from functools import reduce

def soma_quadrados(n):
    return reduce(lambda x,y: x+(y**2), list(range(1,n+1)))

print(soma_quadrados(3))

