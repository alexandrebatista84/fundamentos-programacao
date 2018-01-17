def inverte_dic(dicio):
    new={}

    for i in dicio:
        for x in dicio[i]:

            if x in new:
                new[x]=new[x]+[i]
            else:
                new[x]=[i]

    return new

print(inverte_dic({'a': [1, 2], 'b': [1, 5], 'c': [9], 'd': [4]}))