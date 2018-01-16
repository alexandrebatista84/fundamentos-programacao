def conta_linhas(fich):
    f = open(fich, 'r')
    linhas = f.readlines()
    f.close()
    res = 0
    print(linhas)
    for linha in linhas:
        if linha != "\n":
            res = res + 1
    return res

print(conta_linhas("fich.txt"))