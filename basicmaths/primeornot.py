
def its_prime(n):
    
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
if its_prime(6):
    print("prime")
else:
    print("not prime")