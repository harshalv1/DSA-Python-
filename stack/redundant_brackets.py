
def is_redundant(str):
    stack=[]
    for i in range(len(str)):
        ch=str[i]

        if ch=="(" or ch=="+" or ch=="-" or ch=="*" or ch=="/":
            stack.append(ch)
        else:
            if ch==")":
                is_redundant=True

                top=None
                while top!="(" and len(stack)>0:
                    top=stack.pop()
                    if top=="+" or top=="-" or top=="*" or top=="/":
                        is_redundant=False
                
                if is_redundant==True:
                    return True
                

    return False
                
                               
str1='(a+(b)/c)' #True
str2='(a+c*b)+(c))' #True
str3='(a*b+(c/d))'#False
str4='((a/b))'#True

print(is_redundant(str1))
print(is_redundant(str2))
print(is_redundant(str3))
print(is_redundant(str4))

#space complexity is o(n)
#time complexity is o(n)