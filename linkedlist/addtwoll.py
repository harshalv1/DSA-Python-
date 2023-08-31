# Definition of a singly linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse a linked list
def reverse(head):
    prev = None
    next_node = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Function to insert a new node at the tail of a linked list
def addtoTail(head, tail, data):
    temp = Node(data)
    if head is None:
        head = temp
        tail = temp
    else:
        tail.next = temp
        tail = temp
    return head, tail

# Function to perform addition of two linked lists
def add(first, second):
    carry = 0
    while first or second or carry:
        val1 = 0
        if first:
            val1 = first.data
            first = first.next
        val2 = 0
        if second:
            val2 = second.data
            second = second.next
        
        _sum = val1 + val2 + carry
        digit = _sum % 10
        carry = _sum // 10
        
        head, tail = addtoTail(head, tail, digit)
    
    if carry > 0:
        head, tail = addtoTail(head, tail, carry)
    
    return head

# Function to add two numbers represented by linked lists
def addtwoll(first, second):
    # Reverse both input linked lists
    first = reverse(first)
    second = reverse(second)
    
    # Perform addition of the reversed linked lists
    addition = add(first, second)
    
    # Reverse the final addition result
    ans = reverse(addition)
    
    return ans
