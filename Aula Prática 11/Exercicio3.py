def copia_fic(f1,f2):
    f = open(f1,'r')
    linhas = f.readlines()
    f.close()
    
    f = open(f2,'w')

    if linhas[len(linhas)-1][-1]!='\n':
        linhas[len(linhas)-1]=linhas[len(linhas)-1]+'\n'
    
    for i in range(len(linhas)-1,-1,-1):
        f.write(linhas[i])

    f.close()

copia_fic("fich.txt","fich2.txt")

