# takes a list of integers as input and returns the largest even nber in the list. 
# If there are no even nbers in the list, the function should return None.
# For example, if the input list is [1, 3, 5, 6, 8, 2],the output should be 8 (which is the largest even nber in the list).
def largest_even(my_list):
    even_list=[]
    greatest_even=0
    for n in my_list:
        if n%2==0:
            even_list.append(n)

    for i in range(len(even_list)-1):
        if even_list[i+1]>even_list[i]:
            greatest_even=even_list[i+1]
    return greatest_even






