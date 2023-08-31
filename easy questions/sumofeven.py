#function in Python that takes a list of integers as input and returns the sum of all the even nbers in the list. 
#If the list is empty or contains no even nbers, the function should return 0. 
def sum_evens(list):
    sumofevens=0
    has_even=False
    for i in range(len(list)):   
        if list[i]%2==0:
            sumofevens=sumofevens+list[i]
            has_even=True

    if not list and not has_even:
        return 0
    return sumofevens

total=sum_evens(list=[1,2,3,4])
print(total)

        


