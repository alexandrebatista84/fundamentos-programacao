def ataques_rainhas(j):
    pos_rainha=()
    for i in j:
        if j[i][1]=='rainha':
            pos_rainha=i
    
    l=[]
    for i in j:
        if ((i[0]==pos_rainha[0]) | (i[1]==pos_rainha[1])) & (not j[i][1]=='rainha'):
            l=l+[[j[i][1],i]]

    return l

j = {(1, 'H'): ('branca', 'torre'), (2, 'F'): ('branca', 'peao'), \
(2,'G'): ('branca', 'rei'), (6, 'F'): ('branca', 'bispo'), \
(5,'C'): ('branca', 'rainha'), (6, 'G'): ('preta', 'peao'), \
(7,'F'): ('preta', 'peao'), (8, 'F'): ('preta', 'torre'), \
(8,'G'): ('preta', 'rei'), (2, 'C'): ('preta', 'peao')}

print(ataques_rainhas(j))