n=int(input('n : '))
power=int(input('Power:'))


def exponent(n,power):
    if n==0 and power==0:
        return None
    elif power==0:
        return 1
    
    return n*exponent(n,power-1)

result=exponent(n,power)
print(result) 

    
