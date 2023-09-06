def reverse(word):
    
    reversed_word=""
    
    for i in range(len(word)-1,-1,-1):
        reversed_word=reversed_word+word[i]
        
    
    return reversed_word
    
word="pepper"   
reversed_word=reverse(word)
print(reversed_word)
        


        