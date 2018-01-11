# a)
def perfeito(limite,soma=0,aux=0,res=True):
    if soma==limite:
        return True
    elif soma>limite:
        return False
    else:
        return perfeito(limite,soma+aux,aux+1,res and True)

# b)

def perfeitos_entre(n1,n2):

    if n1>n2:
        return []
    else:
        if perfeito(n1):
            return [n1]+perfeitos_entre(n1+1,n2)
        else:
            return perfeitos_entre(n1+1,n2) 


print(perfeito(28))

print(perfeitos_entre(6,30))