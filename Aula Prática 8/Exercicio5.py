# def espelho(n):
#
#     def espelho_aux(n,res):
#         if n==[]:
#             return res
#         else:
#             return espelho_aux(n[1:], n[0]+res*10)

#     return espelho_aux(list(map(lambda x: int(x), str(n)))[::-1],0)

#def espelho(n):
#   return ''.join(map(str, [int(d) for d in str(n)][::-1]))

#def espelho(n):
#    return int(''.join(list(str(n))[::-1]))


def espelho(n, r=0):
    if n == 0:
        return r
    else:
        return espelho(n//10, (r * 10) + (n % 10))


print(espelho(1234567))