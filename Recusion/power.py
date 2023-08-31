def power(a, b):
    if b == 0:
        return 1
    
    if b%2==0:
        return power(a,b//2)**2
    
    else:
        return power(a,b//2)**2*a

res = power(2,3)
print(res)
