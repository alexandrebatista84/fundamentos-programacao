def num_divisores(n,aux=1):

    if aux>=n:
        return 1
    else:
        if (n%aux==0):
            return 1+num_divisores(n,aux+1)
        else:
            return num_divisores(n,aux+1)


print(num_divisores(20))

print(num_divisores(13))