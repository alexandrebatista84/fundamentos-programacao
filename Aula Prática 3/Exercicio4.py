def area_circulo(r):
    area=3.14*r**2
    return area



def area_coroa (r1, r2):

    if r1 > r2:
        raise ValueError ('Raio exterior menor que raio interior') 

    return area_circulo(r1), area_circulo(r2)



print(area_coroa(2,3))

