def filtra_pares(t):

    if not isinstance(t,tuple):
        raise ValueError("Argumento Inválido")


#    while i < len(t):
#
#        if t[i] % 2 != 0 :
#            t = t[:i] + t[i+1:]
#        else:   
#           i+=1
   
    a=()

    for i in t:
        if i % 2 == 0 :
            a = a + (i,)
    
    return a

print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))
