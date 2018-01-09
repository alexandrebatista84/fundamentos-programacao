def conta_menores(t,n):
    count=0
    for i in t:
        if i<n:
            count+=1
    
    return count

print(conta_menores((3, 4, 5, 6, 7), 5))

print(conta_menores((3, 4, 5, 6, 7), 2))