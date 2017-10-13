n=0
s=0


n=eval(input('Introduza o número de horas de trabalho realizado numa semana: '))
s=eval(input('Introduza o salário por hora: '))

if n<=40:
    print('Salário semanal é igual a ',s*n)
else:
    print ('Salário semanal é igual a ', 40*s+(n-40)*s*2)

