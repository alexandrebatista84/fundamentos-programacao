def reconhece(frase):
    if isinstance (frase, str):
        i, nas = 0, 0
        while i < len(frase) and frase[i] == 'a':
            nas = nas + 1
            i = i + 1
        if nas == 0:
            return False
        else:
            return frase == 'a' * nas + 'b' + 'a' * nas
    else:
        return False

print(reconhece("aabaa"))