def junta_ordenadas(a,b):
    
    l=[]
    i=0
    j=0

    while ((i<len(a)) & (j<len(b))):

        if(a[i]<b[j]):
            l.append(a[i])
            print("a[i] < b[j]",a[i] < b[j],i,j)
            i+=1
            
        else:
            l.append(b[j])
            print("a[i] > b[j]",a[i] > b[j],i,j)
            j+=1
            
    if i<j:
        while i<len(a):
            l.append(a[i])
            i+=1
    else:
        while j<len(b):
            l.append(b[j])
            j+=1
    
    return l

print(junta_ordenadas([0,1,100],[2,4,5]))