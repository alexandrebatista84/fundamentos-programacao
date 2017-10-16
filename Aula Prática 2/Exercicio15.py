digito=eval(input('Introduza um digito\n(para terminar introduza -1)? '))
num=0
while digito!=-1:
    num = num*10+digito
    digito=eval(input('Introduza um digito\n(para terminar introduza -1)? '))

print(num)