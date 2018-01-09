def num(n):
    return  ((n == '1') | (n== '2') | (n== '3') | (n== '4'))
    
def letra(l):
    return ((l == 'A') | (l== 'B') | (l== 'C') | (l== 'D'))

def numeros(n):
    for i in n:
        if (not (num(i))):
            return False
    return True

def letras(n):
    for i in n:
        if (not (letra(i))):
            return False
    return True

def reconhece (variavel):
    for i in range(1,len(variavel)):
        if ((letras(variavel[:i])) & (numeros(variavel[i:]))):
            return True
    return False 


print(reconhece('ABC12C'))