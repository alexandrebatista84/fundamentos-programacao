def misterio(x, n):
    if n == 0:
        return 0
    else:
        return x * n + misterio(x, n - 1)

print(misterio(2,6))

# a) soma dos n primeiros multiplos de x

# b) misterio(2,3)
#    2 * 3 + misterio (2,2)
#    2 * 3 + (2 * 2 + misterio (2,1))
#    2 * 3 + (2 * 2 + (2 * 1 + misterio (2,0)))
#    2 * 3 + (2 * 2 + (2 * 1 + 0))
#    2 * 3 + (2 * 2 + 2)
#    2 * 3 + 6
#    12

# c) processo recursivo
# Num processo recursivo existe uma fase de expansão correspondente à construção
# de uma cadeia de operações adiadas, seguida por uma fase de contracção 
# correspondente à execução dessas operações

def mult(x,n):

    def aux_mul(x,n_iter,res):

        if n_iter==0:
            return res
        else:
            return aux_mul(x,n_iter-1,res+x*n_iter)

    return aux_mul(x,n,0)

print(mult(2,6))