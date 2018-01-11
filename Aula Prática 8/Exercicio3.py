# a)
def numero_digitos(n):

    if n//10==0:
        return 1
    else:
        return 1+numero_digitos(n//10)

# b)
def numero_digitos(n):

    def numero_digitos_aux(n,res):
        if n//10==0:
            return res
        else:
            return numero_digitos_aux(n//10,res+1)

    return numero_digitos_aux(n,1)

# c)
def numero_digitos(n):
    count=1
    while n//10!=0:
        count+=1
        n=n//10
    return count

print(numero_digitos(123))