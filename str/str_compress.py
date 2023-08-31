def compression(chars):
    n=len(chars)
    count=1 #started the count with 1 as each character would be present in the array at least once 
    write=0 # represents the index in which we are writing/adding the characters 
    anchor=0 # represents the start of a group of characters
    
    for i in range(1,n): # we start the range from one as we cannot compare the previous character if we start from index 0 and it goes until n-1 range doesn't include the last index 
        if chars[i]==chars[i-1]: # if the characters are same we increment the count 
            count=count+1
        else:
            chars[write]=chars[anchor] # the anchor was on the 0th index so that would be added to chars 
            write=write+1 # increment the write variable 
            if count>1:
                count_str=str(count) # converting the string to str 
                for digit in count_str: # for every digit that is in str string 
                    chars[write]=digit # that digit is added to chars 
                    write=write+1 
            anchor=i # anchor value is updated to the current value as we have two characters which are not similar to each other that means we have found a new group/single  letter 
            count=1 #count is reset to 1 as we have found a new group 
            
    chars[write]=chars[anchor] # handling of the last character as there is not next group to be compared it with and then this character to be added 
    write=write+1
    if count>1:
        count_str=str(count)
        for digit in count_str:
            chars[write]=digit
            write=write+1                
    return write #we return the length of compressed string 
    #return chars[:write] #this will return the chars string until the write index 
chars=['a','b','b','c','c','c','d','d','d','d']
print(compression(chars))