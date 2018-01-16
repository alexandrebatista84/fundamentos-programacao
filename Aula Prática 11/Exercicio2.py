def vogais(v):
    return ((v=='a') | (v=='e') | (v=='i') | (v=='o') | (v=='u'))

def conta_vogais(ficheiro):
    f = open(ficheiro, 'r')
    linhas = f.readlines()
    f.close()
    dicionario={}

    for i in linhas:
        for x in i:
            if vogais(x):
                if x in dicionario:
                    dicionario[x]=dicionario[x]+1
                else:
                    dicionario[x]=1
    return dicionario

print(conta_vogais("fich.txt"))