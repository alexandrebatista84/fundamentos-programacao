def metabolismo(dicionario):
    met_basal={}

    for i in dicionario:
        
        if dicionario[i][0]=='M':
            met_basal[i]=66+6.3*dicionario[i][3]+12.9*dicionario[i][2]+6.8*dicionario[i][1]
        else:
            met_basal[i]=655+4.3*dicionario[i][3]+4.7*dicionario[i][2]+4.7*dicionario[i][1]

    return met_basal


d={'Maria' : ('F', 34, 1.65, 64), 'Pedro': ('M', 34, 1.65, 64), 'Ana': ('F', 54, 1.65, 120), 'Hugo': ('M', 12, 1.82, 75)}
print(metabolismo(d))