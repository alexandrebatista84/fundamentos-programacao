def sublistas(l):
    if (not isinstance(l,list)) | (len(l)==0):
        return 0
    else:
        
        if (isinstance(l[0],list)):
            return (1+sublistas(l[0])+sublistas(l[1:]))
        else:
            return sublistas(l[1:])


print(sublistas ([[1], 2, [3]]))
print(sublistas([[[[[1]]]]]))
print(sublistas(['a', [2, 3, [[[1]], 6, 7], 'b']]))