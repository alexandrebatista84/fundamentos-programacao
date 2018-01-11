def somatorio(l_inf, l_sup, calc_termo, prox):
    soma = 0
    while l_inf <= l_sup:

        print("isto é o limite inferior -> ",l_inf)
        print("isto é o limite superior -> ",l_sup)
        print("isto é a soma -> ",soma)
        
        soma = soma + calc_termo(l_inf)
        l_inf = prox(l_inf)

        print("isto é o limite inferior -> ",l_inf)
        print("isto é o limite superior -> ",l_sup)
        print("isto é a soma -> ",soma)
    return soma

#rint(somatorio(9, 21, lambda x: x ** 2, lambda x: x + 3))
#somar os quadrados dos múltiplos de 3 entre 9 e 21

#print(somatorio(4, 500, lambda x: x, lambda x: x + 1))
#somar todos os numeros entre 4 e 500

#print(somatorio(5, 500, lambda x: x * x, lambda x: x + 5))
#somar os quadrados dos múltiplos de 5 entre 5 e 500

print(somatorio(1, 5, lambda x: somatorio(1, x, lambda x: x, lambda x: x+1), lambda x: x+1))
