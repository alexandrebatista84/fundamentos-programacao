def parte (lst, el):

    def parte_aux(lst, el, menores, maiores):
        if lst == []:
            return [menores, maiores]
        elif lst[0] < el:
            return parte_aux(lst[1:], el, menores + [lst[0]], maiores)
        else:
            return parte_aux(lst[1:], el, menores, maiores + [lst[0]])

    return parte_aux(lst, el, [], [])

print(parte([3, 5, 1, 4, 5, 8, 9], 4))