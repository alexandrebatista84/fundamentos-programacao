def num_para_seq_cod (n):

    if not (isinstance(n,int)):
        raise ValueError ("Não é um número inteiro")

    t=()

    while n!=0:
        if n%10%2==0:
            if n%10==8:
                t = (0,) + t
            else:
                t = (n%10+2,) + t
        else:
            if n%10==1:
                t = (9,) + t
            else:
                t = (n%10-2,) + t
        n=n//10

    return t

print(num_para_seq_cod(1234567890))
        
   