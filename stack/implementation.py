class Stack: #implementation using arrays
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("stack underflow")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("stack is empty")
    
    def is_empty(self):
        return len(self.items)==0

    def size (self):
        return len(self.items)

#example 
stack=Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)

print("Size",stack.size())
print("Pop:",stack.pop())
print("Peek:",stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())

# stack implementation using linked lists 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Link the new node to the current top node
        new_node.next = self.top
        # Update the top to point to the new node
        self.top = new_node
    
    def pop(self):
        if not self.is_empty():
            # Retrieve the data of the top node
            ans = self.top.data
            # Move the top pointer to the next node, effectively removing the current top
            self.top = self.top.next
            return ans 
        else:
            print("stack empty")
    
    def peek(self):
        if not self.is_empty():
            # Return the data of the top node without removing it
            ans = self.top.data
            return ans
        else:
            print("stack empty")
    
    def is_empty(self):
        # Check if the stack is empty by examining the top pointer
        return self.top == None
    
    def size(self):
        count = 0
        curr = self.top
        # Iterate through the linked list and count the nodes
        while curr:
            count += 1
            curr = curr.next
        return count 

# Create a new stack instance
stack = Stack()
# Push elements onto the stack
stack.push(5)
stack.push(10)
stack.push(15)

# Display the size of the stack
print("Size:", stack.size())
# Pop an element from the stack
print("Pop:", stack.pop())
# Peek at the top element of the stack
print("Peek:", stack.peek())
