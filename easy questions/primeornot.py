n=int(input("What;s the nber:"))
def its_prime(n):
    
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
if its_prime(n):
    print("Prime")
else:
    print("Not prime")