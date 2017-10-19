def amigas (p1,p2):

    if (not isinstance(p1, str)) & (not isinstance(p2, str)):
        raise ValueError("Doesn't look like a string!")

    if p1 == p2:
        return True
    
    if len(p1)!=len(p2):
        return False

    count=0
    i=0

    while i<len(p1):
        if p1[i]!=p2[i]:
            count+=1
        i+=1
    
    if count/len(p1)<0.1:
        return True
    else:
        return False

    

print(amigas('amigas','asigos'))