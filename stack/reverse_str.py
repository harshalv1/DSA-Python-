
str='Peace'

stack=[]

for i in range(len(str)):
    ch=str[i]
    stack.append(ch)

new_str=''

while len(stack)>0:
    ch=stack[-1]
    new_str=new_str+ch
    stack.pop()
    
print(new_str)


    