# a)
def quadrado_natural(n):

    def quadrado_natural_aux(n):
        if n<=0:
            return 0
        else:
            if n%2!=0:
                return n+quadrado_natural_aux(n-1)
            else:
                return quadrado_natural_aux(n-1)

    return quadrado_natural_aux(n+n)

# b)
def quadrado_natural(n):

    def quadrado_natural_aux(n,res):
        if n<=0:
            return res 
        else:
            if n%2!=0:
                return quadrado_natural_aux(n-1,res+n)
            else:
                return quadrado_natural_aux(n-1,res)

    return quadrado_natural_aux(n+n,0)

# c)
def quadrado_natural(n):
    sum=0
    for i in range(n+n+1):
        if i%2!=0:
            sum=sum+i
    
    return sum


print(quadrado_natural(3))