def codifica(n):
    string=''
    i=0

    while i<len(n):
        if i%2==0:
            string=string+n[i]
        i+=1

    i=0   
    while i<len(n):
        if i%2!=0:
            string=string+n[i]
        i+=1

    return string 


def descodifica(n):

    if len(n)%2==0:
        meio=len(n)//2
    else:
        meio=len(n)//2+1

    string=''
    i=0
    
    while i<meio:
        string=string+n[i]
        if (i+meio<len(n)):
            string=string+n[i+meio]
        
        i+=1

    return string 

print(descodifica("acebdf"))