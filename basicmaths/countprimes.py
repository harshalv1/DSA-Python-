
n=int(input("What;s the nber:"))

def isprime(n):
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def prime_count(n):
    prime_count=0
    for i in range(2,n):
        if isprime(i):
            prime_count=prime_count+1
    print(prime_count)
prime_count(n)


    

