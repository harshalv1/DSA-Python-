
def check_pal(input_word): 
    s=0
    e=len(input_word)-1

    while s<=e:
        if input_word[s].lower()!=input_word[e].lower(): 
            return False
        s=s+1
        e=e-1
    return True

input_word="Nayan"
print(check_pal(input_word))
        
        