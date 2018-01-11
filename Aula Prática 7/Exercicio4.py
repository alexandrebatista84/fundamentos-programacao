def todos_lista(lista, pred):
    l1=list(filter(pred, lista))
    return lista==l1

print(todos_lista([4, 5, 6], lambda x: x > 5))
print(todos_lista([4, 5, 6], lambda x: x >= 4))