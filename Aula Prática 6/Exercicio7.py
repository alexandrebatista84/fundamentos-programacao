def pertence(l,n):

    if len(l)==0:
        return False
    else:
        if l[0]==n:
            return True
        else:
            return pertence(l[1:],n)

print(pertence([3, 4, 5], 2))
print(pertence([3, 4, 5], 5))