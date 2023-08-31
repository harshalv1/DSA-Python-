
def revstr(input_string): 
    s=0
    e=len(input_string)-1

    while s<e:
        input_string[s],input_string[e]=input_string[e],input_string[s] #swapping of every character 
        s=s+1
        e=e-1

input_string=list("apple") #the input is a list of characters 
revstr(input_string) # function call 
print("Reversed string: ","".join(input_string)) #.join method joins the reversed string with the empty string / "" as a separator 