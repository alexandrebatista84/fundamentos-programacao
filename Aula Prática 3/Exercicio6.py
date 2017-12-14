def bissexto(n):
    if ((n%4==0) & (n%400==0)):
        return True
    else:
        if ((n%4==0) & (n%100!=0)):
            return True
        else:
            return False


print(bissexto(1984))
print(bissexto(1985))
print(bissexto(2000))