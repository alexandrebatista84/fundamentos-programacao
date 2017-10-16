def explode (n): 
    

    if not isinstance(n,int):
            raise ValueError ('explode: argumento não inteiro')
    
    while n//10 == 0:
        t[i] = t[i] + n%10
        i+=1
        n=n//10
        
    return t

t=()
print(explode(123245))