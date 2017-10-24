def junta_ordenadas(a,b):

    l=[]
    x=0
    y=0
    
    while ((y < len (b)) and (x < len(a))):
        if a[x]<b[y]:
            l.append(a[x])
            x+=1
        else:
            l.append(b[y])
            y+=1
    return l

print(junta_ordenadas([2,5,90], [91,92,93,94]))