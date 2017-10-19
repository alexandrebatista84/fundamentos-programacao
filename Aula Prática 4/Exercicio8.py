
def num(n):

        if ((n == 1) | (n== 2) | (n== 3) | (n== 4)):
            return True
        else:
            return False

def numeros (n):

    t=()

    if type(n) != int:
        return False
    else:
        while n!=0:
            t = (n%10,)+t 
            n=n//10
    
    flag=0

    for i in t:
        if (not num(t[i])):
           flag=1
           break

    if flag==1:
        return False
    else:
        return True 

def letra(l):

    if ((l == 'A') | (l== 'B') | (l== 'C') | (l== 'D')):
        return True
    else:
        return False

def letras(l):
    i=0
    flag=0
    while i < len(l):

        if (not letra(l[i])):
            flag=1
            break
        else:
            i+=1

    if flag==1:
        return False
    else:
        return True


def reconhece (variavel):

    if (letras(variavel) | numeros(variavel)):
        print("são so letras") 

print(reconhece('ACD12323'))