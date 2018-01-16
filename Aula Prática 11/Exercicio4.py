def concatena(f1,f2):
    f = open(f1,'r')
    linhas = f.readlines()
    f.close()
    
    f = open(f2,'a')
    for i in linhas:
        f.write(i)
    f.close

concatena("fich.txt","fich2.txt") 