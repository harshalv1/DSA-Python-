def return_even(inputlist):#function that takes a list and returns list that contains only the even nbers from the original list. 
    new_list=[]

    for i in inputlist:
        if i%2==0:
            new_list.append(i)
    return new_list