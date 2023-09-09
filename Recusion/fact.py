
n=int(input("n:"))

def factorial(n):
    if n==0: #base case 
        return 1
    
    return n*factorial(n-1) #recursive call 

result=factorial(n)
print(result)