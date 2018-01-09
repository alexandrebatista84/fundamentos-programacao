def troca_occ_lista(lista,a,b):

    if len(lista)==0:
        return lista
    else:
        if lista[0]==a:
            return [b]+troca_occ_lista(lista[1:],a,b)
        else:
            return [lista[0]]+troca_occ_lista(lista[1:],a,b)

print(troca_occ_lista([(2, 3), 'a', 3, True, 5], 'a', 2))
print(troca_occ_lista([(2, 3), 'a', 3, True, 5], False, 4))
print(troca_occ_lista([], False, 4))