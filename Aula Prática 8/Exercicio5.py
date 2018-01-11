def espelho(n):

    def espelho_aux(n,res):
        if n==0:
            return res
        else:
            return espelho_aux(n//10, res+[n%10])

    return espelho_aux(n,[])
    
print(espelho(123))