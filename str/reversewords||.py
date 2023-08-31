
def reverse(sentence):
    splitting= sentence.split()
    
    nw_ls=[]
    for word in splitting:
        rev_word=word[::-1]
        nw_ls.append(rev_word)
    
    rev_sentence=" ".join(nw_ls)
    return rev_sentence
    
sentence="Hey! You are starting to win"
print(reverse(sentence))