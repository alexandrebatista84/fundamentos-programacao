count=0
n_notas=0

n=float(input('Introduza a nota do aluno\n(introduza -1 para sair) '))

while n != -1:
    n_notas+=1
    if n >= 9.5:
        count+=1
    n=float(input('Introduza a nota do aluno\n(introduza -1 para sair) '))   

print("Número de Notas Positivas: ",count)
print("Percentagem de Notas Positivas: ", count/n_notas)