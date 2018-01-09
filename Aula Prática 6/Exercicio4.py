def soma_n_vezes(a,b,n):
    
    if n==0:
        return a
    else:
        return b+soma_n_vezes(a,a,n-1)

print(soma_n_vezes(3,2,5))