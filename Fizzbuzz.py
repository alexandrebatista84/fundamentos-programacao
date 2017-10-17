i=1

while i <= 100:

    if i % 3 == 0 :
        print ("fizz")
        i+=1

    elif i % 5 == 0:
        print ("buzz")
        i+=1

    elif i % 3 == 0 & i % 5 == 0:
        print ("fizzbuzz")
        i+=1
    
    else: 
        print(i)
        i+=1
    
    

