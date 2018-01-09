def subtrai(l1,l2):
    if len(l1)==0:
        return l1
    else:
        if l1[0] in l2:
            return subtrai(l1[1:],l2)
        else:
            return [l1[0]]+subtrai(l1[1:],l2)

print(subtrai([2, 3, 4, 5], [2, 3]))
print(subtrai([2, 3, 4, 5], [6, 7]))