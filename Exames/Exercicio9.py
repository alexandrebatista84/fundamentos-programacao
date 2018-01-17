from functools import reduce

def soma_quadrados(l):

    return reduce(lambda x,y: x+y,list(map(lambda x:x**2,l)))

print(soma_quadrados([1,2,3,4]))