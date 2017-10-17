def filtra_pares(t):
    i=0
    while i < len(t):

        if t[i] % 2 != 0 :
            t = t[:i] + t[i+1:]
        else:   
            i+=1   
    
    return t

print(filtra_pares((2, 5, 6, 7, 9, 1, 8, 8)))