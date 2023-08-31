
n=int(input("No: "))

def count(n):
    if n==0:
        return # exits the function 
     
    count(n-1) #this function is called until the base case is met 
    print(n) #first at n=1 1 is printed then 2 then 3 then 4 until n
    

count(n)
