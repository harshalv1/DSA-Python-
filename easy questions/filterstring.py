
def filter_string(mylist):# takes a list of strings as input and returns a new list that contains only the strings that have length greater than or equal to 5.
    newlist=[]
    for i in mylist:
        if len(i)>=5:
            newlist.append(i)
    return newlist