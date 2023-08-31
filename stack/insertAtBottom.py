def solve(inputstack,num):

    if len(inputstack)==0:
        inputstack.append(num)
        return 
    
    popped_element=inputstack.pop()
    solve(inputstack,num)
    inputstack.append(popped_element)

def insertAtBottom(inputstack,num):
    solve(inputstack,num)


inputstack=[]
inputstack.append(1)
inputstack.append(2)
print(inputstack)
insertAtBottom(inputstack,3)
print(inputstack)