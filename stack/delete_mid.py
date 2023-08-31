class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def solve(stack, count, size):
    if count == size // 2:
        stack.pop()  # Remove the middle element from the stack
        return
    
    num = stack.pop()  # Pop the top element of the stack
    solve(stack, count + 1, size)  # Recur for the remaining elements
    stack.push(num)  # Push the element back onto the stack

def delete_mid(stack, size):
    count = 0
    solve(stack, count, size)  # Call the solve function to delete the middle element

stack = Stack()

# Push elements onto the stack
stack.push(5)
stack.push(1)
stack.push(7)
stack.push(2)
stack.push(6)

print("Original Stack:", stack.items)

# Delete the middle element
delete_mid(stack, stack.size())

print("Stack after deleting middle element:", stack.items)
#--------------------------------------------------------------------------------
#same solution but without creating a class stack
def solve(inputStack,count,N):
    if count==len(inputStack)//2:
        inputStack.pop()
        return 
    
    num=inputStack.pop()
    solve(inputStack,count+1,N)
    inputStack.append(num)

def deleteMiddle(inputStack, N):
    count=0
    
    solve(inputStack,count,N)
    
inputStack=[]
inputStack.append(1)
inputStack.append(2)
inputStack.append(3)
print(inputStack)
deleteMiddle(inputStack,3)
print(inputStack)
