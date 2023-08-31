
def sayit(n):
    if n==0: #the base case is the number becomes zero 
        return # then we exit the function and no longer recursively call 
    
    digit=n%10 #extracting the digit by modulus operator which would give us the remainder/digit
    n=n//10 #as we have extracted the digit the new number is n floor division 10 which is the quoteint 
    
    sayit(n) #function call (recursive)
    
    print(arr[digit],end=" ") # this statement prints the value corresponding to the index digit 
    

arr=['zero','one','two','three','four','five','six','seven','eight','nine'] #global array named arr 
n=int(input("What is the number you want me to say:")) 
sayit(n)