def soma_digitos (a):
    
    if a=='':
        return 0
    else:
        return int(a[0]) + soma_digitos(a[1:])
    
#print(soma_digitos('1250'))

def digit(str):

    if str == '':
        return False

    if len(str)==1:
        return ('0' <= str[0] <= '9')

    return ('0' <= str[0] <= '9') and digit(str[1:])


#print(digit('1349236e4325463274a23'))



def parse_expr(line):
    lst=[]

    i=len(line)-1

    while i>=0:
        if not digit(line[i:]):
            lst.append(int(line[i+1:]))
            line=line[:i]
        
        if i==0 and digit(line):
            lst.append(int(line))
        
        i=i-1

    print(lst)

    return sum(lst)


print (parse_expr("30+10+1+2+3+4+5+6+7+8+9+10"))