def piatorio(l_inf,l_sup):

    if l_sup<l_inf:
        return 1
    else:
        return l_sup*piatorio(l_inf,l_sup-1)

print(piatorio(2,4))