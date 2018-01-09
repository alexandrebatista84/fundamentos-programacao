def maior(lista):

    def maior_aux(lista,maior):
        if lista==[]:
            return maior
        elif (maior<lista[0]):
            return maior_aux(lista[1:],lista[0])
        else:
            return maior_aux(lista[1:],maior)

    return maior_aux(lista,0)

print(maior([5, 3, 8, 1, 9, 2]))