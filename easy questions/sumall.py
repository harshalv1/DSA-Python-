
def sumofevens(my_list): #Write a Python function that takes a list of integers as input and returns the sum of all the even nbers in the list.  give me a solution to this problem
    sumofns=0
    for n in my_list:
        if n%2==0:
            sumofns=sumofns+n
    return sumofns

