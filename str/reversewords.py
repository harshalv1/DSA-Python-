def reverse_sentence():
    sentence = input("What would you like to reverse: ")
    
    split_sentence = sentence.split()
    
    reversed_sentence=" ".join(split_sentence[::-1])

    return reversed_sentence

reversed_text = reverse_sentence()
print(reversed_text)
    