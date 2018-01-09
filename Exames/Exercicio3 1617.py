def soma_divisores(n):
    
    res=0

    for i in range (1,n+1):
        if n%i==0:
            res=res+i
    
    return res

print(soma_divisores(20))

print(soma_divisores(13))