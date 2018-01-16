from random import randint

# a)
def baralho():

    bar=[]
    valores=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipe=['esp','cop','our','pau']
    

    for x in naipe:
        for y in valores:
            bar.append({'np':x,'vlr':y})
    return bar

# b)
def baralha(l):
    b=0
    for i in range (0, len (l)):
        
        a=randint(0,51)
        b=l[i]
        l[i]=l[a]
        l[a]=b

    return l

# c)
def distribui(l):
    a=[[],[],[],[]]
    tamanho=52
    for i in range (0,len(a)):
        for x in range (13): 
            tamanho=tamanho-1        
            num=randint(0,tamanho)
            a[i].append(l[num])
            del(l[num])
    return a

print(distribui(baralha(baralho())))