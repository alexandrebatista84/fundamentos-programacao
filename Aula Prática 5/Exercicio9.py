def racaman(n):

    l=[0]
    i=1

    while i<n:
        
        if ((l[i-1]-i>0) & (not (l[i-1]-i) in l)):
            l.append(l[i-1]-i)
        elif (not (l[i-1]+i) in l):
            l.append(l[i-1]+i)
        i+=1
    return l

print(racaman(15))
