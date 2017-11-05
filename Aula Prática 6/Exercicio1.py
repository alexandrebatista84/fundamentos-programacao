def soma_digitos_pares(n):
    if n==0:
        return 0
    else:  
        if ((n%10%2)==0):            
            return soma_digitos_pares(n//10) + n % 10
        else:
            return soma_digitos_pares(n//10)
  
print(soma_digitos_pares(1234))