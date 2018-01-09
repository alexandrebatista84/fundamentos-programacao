def dia_da_semana (d,m,a):

    if ((m==1) | (m==2)):
        m=m+12
        a=a-1
        
    k=modulo(a,100)
    j=chao(a/100)
    
    h=modulo((d + chao((13*m+13)/5) + k + chao(k/4) + chao(j/4) - 2*j), 7)

    diasdasemana=('sábado','domingo','segunda','terça','quarta','quinta','sexta')

    return diasdasemana[h]

def chao(x):
    x=x//1
    x=int(x)
    return x

def modulo(a,b):
    return a%b

print(dia_da_semana(1,1,2000))

