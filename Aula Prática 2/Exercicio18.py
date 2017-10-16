n=int(input('Introduza um numero inteiro:\n'))
temp=0
count=0

while n // 10 != 0:
    if n % 10 == 0:
        count +=1
    n=n//10

print(count)

