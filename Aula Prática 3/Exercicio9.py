def serie_geom(r,n):

    if ((type(r)!= int) | (type(n)!= int) | (n<0)):
        return ValueError ("serie_geom: argumento incorrecto")    

    if n==0:
        return 1
    else:
        return r**n+serie_geom(r,n-1)

print(serie_geom(100,-1))