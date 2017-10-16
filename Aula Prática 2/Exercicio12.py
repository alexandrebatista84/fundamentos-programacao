def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = eval(input('Qual o valor de x:\n ? '))
n = eval(input('Qual o valor de n:\n ? '))
soma=1
while n>=1:
    soma=soma+(x**n/factorial(n))
    n=n-1

print(soma)
