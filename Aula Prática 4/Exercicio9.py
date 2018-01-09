def ter(n):
    for i in n:
        if (not i=='c'):
            return False 
    return True 

def seg(n):
    if len(n)<3:
        return False
    if ((n[0]=='b') & (ter(n[1:len(n)-1])) & (n[len(n)-1]=='b')):
        return True
    if ((n[0]=='b') & (seg(n[1:len(n)-1])) & (n[len(n)-1]=='b')):
        return True
    return False 

def reconhece(n):
    if len(n)<3:
        return False
    if ((n[0]=='a') & (seg(n[1:len(n)-1])) & (n[len(n)-1]=='a')):
        return True
    if ((n[0]=='a') & (reconhece(n[1:len(n)-1])) & (n[len(n)-1]=='a')):
        return True
    return False 


print (reconhece('abcccccba'))