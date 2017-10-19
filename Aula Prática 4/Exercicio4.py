def num_para_seq_cod (n):

    if not (isinstance(n,int)):
        raise ValueError ("Não é um número inteiro")

    t=()

    while n!=0:
        t =  (n%10,) + t
        n=n//10
   
    tpares=()

    for i in range(0,len(t)):
        if (t[i]%2==0 & t[i] == 0):
            tpares= tpares + (t[i],)


    timpares=()

    for i in range(0,len(t)):
        if t[i]%2!=0:
            timpares= timpares + (t[i],)

    tfinal=()
    x=0
    y=0
    
    for i in range(0,len(t)):

        if t[i]%2==0:
            
            if x==len(tpares)-1:
                tfinal = tfinal + (tpares[0],)
            else: 
                tfinal = tfinal + (tpares[x+1],)
                x+=1
        else:
            
            if y==0:
                tfinal = tfinal + (timpares[len(timpares)-1],)
                y+=1
            else: 
                tfinal = tfinal + (timpares[y-1],)
                y+=1
                
    return tfinal

print(num_para_seq_cod(1234567890))