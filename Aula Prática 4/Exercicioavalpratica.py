def duplica (t):
    a=()
    for i in range (0,len(t)):

        a = a + (t[i],) + (t[i],)
        
    return a

print (duplica((1,2,3)))