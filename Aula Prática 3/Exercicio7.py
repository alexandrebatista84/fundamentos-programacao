def bissexto(n):
    if ((n%4==0) & (n%400==0)):
        return True
    else:
        if ((n%4==0) & (n%100!=0)):
            return True
        else:
            return False

def dias_mes (mes,ano):

    if not(mes.islower()):
        return ValueError ("ValueError: Mês não existe")

    if (mes=='fev'):
        if bissexto(ano):
            return 29
        else:
            return 28


    if ((mes=='jan') | (mes=='mar') | (mes=='mai') |(mes=='jul') |(mes=='ago') | (mes=='out') | (mes=='dez')):
        return 31

    if ((mes=='abr') | (mes=='jun') | (mes=='set') |(mes=='nov')):
        return 30

