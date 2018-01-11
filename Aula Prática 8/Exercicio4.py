
def e_capicua(n):

    def e_capicua_aux(n,res):
       
        if len(n)<2:
            return res
        else:
            return e_capicua_aux(n[1:-1],(res and n[0]==n[-1]))
        
    return e_capicua_aux(list(str(n)), True)
   

def numero_digitos(n):

    if n//10==0:
        return 1
    else:
        return 1+numero_digitos(n//10)


print(e_capicua(1221))
