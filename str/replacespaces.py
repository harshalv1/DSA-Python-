
def replace_space():
    sentence=input("Give me the input: ")
    
    replaced_sentence=""
    
    for ch in sentence:
        if ch==" ":
            replaced_sentence=replaced_sentence+"@"
        else:
            replaced_sentence=replaced_sentence+ch
    
    return replaced_sentence

print(replace_space())
            