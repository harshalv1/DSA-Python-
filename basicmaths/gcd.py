def gcd(a,b): #finding the greatest common divisor gcd(a,b)==gcd(a-b,b) or gcd(a%b,b) eventually they become the same 
                #and then the non zero value is the gcd 
    if a==0 and b==0:
        return 0
    if a==0:
        return b
    if b==0:
        return a
        
    while a==b:
        if a>b:
            return a-b
        elif b>a:
            return b-a

    return a

our_gcd=gcd(5,10) #gcd of 5 and 10 will be 5 
print(our_gcd)
