
#that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a' (case-insensitive). 
def strings_withA(input_list):
    new_list=[]
    for word in input_list:
        if "a" in word  or "A" in word:
            new_list.append(word)
    return new_list

