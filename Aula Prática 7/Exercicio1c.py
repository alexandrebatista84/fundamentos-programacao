def piatorio(l_inf,l_sup):

    if l_sup<l_inf:
        return 1
    else:
        return l_sup*piatorio(l_inf,l_sup-1)

def factorial(n):

    return piatorio(1, n)

print(factorial(0))