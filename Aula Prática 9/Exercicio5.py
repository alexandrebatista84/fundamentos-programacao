def conta_palavras(texto):
    
    palavras={}
    texto=texto.split()
 
    for i in range (0,len(texto)):
        if texto[i] in palavras:
            palavras[texto[i]]=palavras[texto[i]]+1
        else:
            palavras[texto[i]]=1
    return palavras


cc = 'a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha'
print(conta_palavras(cc))
