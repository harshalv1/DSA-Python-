
def ispalindrome(word,s,e):
    if s>e:
        return True
    
    if word[s]!=word[e]:
        return False
    
    else:
        return ispalindrome(word,s+1,e-1)


word="nayan"
if ispalindrome(word,0,len(word)-1):
    print("Palindrome")
else:
    print("Not a palindrome")

#  def ispalindrome(word, i):
#      if i >= len(word) // 2:
#          return True
    
#      if word[i] != word[len(word) - i - 1]:
#          return False
    
#      return ispalindrome(word, i + 1)


#  word = "nayan"
#  if ispalindrome(word, 0):
#      print("Palindrome")
#  else:
#      print("Not a palindrome")
