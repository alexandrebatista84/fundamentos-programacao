def concentra(op, num):
    if num < 10:
        return num
    else:
        return op(num % 10, concentra(op, num // 10))

def produto(n):
    return concentra(lambda x,y: x*y,n)

print(produto(24))