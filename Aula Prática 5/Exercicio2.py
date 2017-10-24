def remove_multiplos(a,b):
    l=[]
    for i in a:
        if i%b!=0:
            l.append(i)
    return l

print(remove_multiplos([2,3,5,9,12,33,34,45],3))