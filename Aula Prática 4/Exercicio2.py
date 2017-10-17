def explode (n): 
    t=()
    if not isinstance(n,int):
            raise ValueError ('explode: argumento não inteiro')
    
    while n!=0:
        t = (n%10,)+t 
        n=n//10
                
    return t


print(explode(123245))