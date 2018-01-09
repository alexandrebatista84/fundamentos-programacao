def apenas_digitos_impares(a):

    if a==0:
        return 0
    else:
        if ((a%10%2)!=0):
            return(a%10+10*apenas_digitos_impares(a//10))
        else:
            return(apenas_digitos_impares(a//10))

print(apenas_digitos_impares(123456789))

