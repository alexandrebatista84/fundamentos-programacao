def nenhum_p(n,pred):
    if n>0:
        if not pred(n):
            return True and nenhum_p(n-1,pred)
        else:
            return False
    else:
        return True

print(nenhum_p(87, lambda x: x % 100 == 0))

print(nenhum_p(187, lambda x: x % 100 == 0))