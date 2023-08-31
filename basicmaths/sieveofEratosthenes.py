def count_prime(n):
    if n<=2:
        return 0 
    
    prime=[True]*n #every nber is assigned as prime nber at the beginning 
    prime[0]=prime[1]=False #with exceptions 0 and 1
    
    count=0 # we do not want to reset the value of count after each iteration therefore it is outside the loop 
    for i in range(2,n):
        if prime[i]: 
            count=count+1 #incrementing the count if prime nber is found 
            for j in range(i*i,n,i): #marking the multiples of prime nber 
                prime[j]=False #as false the loop iterates from i*i till n with i as the step value 
    return count

res=count_prime(10)
print(res)


#Time-complexity 
 #n/2+n/3+n/5+n/7+n/11... (this is a harmonic progression)
 # o(n(log(logn))