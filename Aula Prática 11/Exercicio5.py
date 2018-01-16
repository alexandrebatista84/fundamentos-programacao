def procura(palavra,f1):
    f = open(f1,'r')
    linhas = f.readlines()
    f.close()
    
    for i in range(0,len(linhas)): 
        if palavra in linhas[i]:
            print(linhas[i][0:-1])
            


procura("Carvalho","fich2.txt") 