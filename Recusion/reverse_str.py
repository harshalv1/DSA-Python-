
def reverse(word,s,e):
    if s>e:
        return word
    
    word[s],word[e]=word[e], word[s]
    s=s+1
    e=e-1
    
    return reverse(word,s,e)

word=list("gabbar")
re=reverse(word,0,len(word)-1)
print("".join(str(letter) for letter  in word))