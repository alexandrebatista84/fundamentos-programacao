from functools import reduce

def junta_listas(lista):
    return list(reduce(lambda x,y: x+y, lista))


print(junta_listas([[1, 2], [[3]], [4, 5]]))
