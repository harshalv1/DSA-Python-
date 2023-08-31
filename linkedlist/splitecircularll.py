class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the midpoint of the circular linked list
def give_mid(head):
    length = 0
    curr = head
    while curr != None:
        curr = curr.next
        length = length + 1
    
    if length % 2 == 0:
        mid = length // 2
    else:
        mid = (length // 2) + 1
    return mid

# Function to split a circular linked list into two halves
def split(head):
    mid = give_mid(head)

    curr = head
    count = 0

    # Traverse to the midpoint node
    while count < mid:
        curr = curr.next
        count = count + 1
    
    nextn = curr.next
    head1 = head
    curr.next = head  # Circular linkage for the first half

    head2 = nextn
    curr = nextn

    # Traverse to the last node of the second half
    while curr != head:
        curr = curr.next
    
    curr.next = head2  # Circular linkage for the second half

    return head1, head2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the midpoint of the circular linked list
def give_mid(head):
    length = 0
    curr = head
    while curr != None:
        curr = curr.next
        length = length + 1
    
    if length % 2 == 0:
        mid = length // 2
    else:
        mid = (length // 2) + 1
    return mid

# Function to split a circular linked list into two halves
def split(head):
    mid = give_mid(head)

    curr = head
    count = 0

    # Traverse to the midpoint node
    while count < mid:
        curr = curr.next
        count = count + 1
    
    nextn = curr.next
    head1 = head
    curr.next = head  # Circular linkage for the first half

    head2 = nextn
    curr = nextn

    # Traverse to the last node of the second half
    while curr != head:
        curr = curr.next
    
    curr.next = head2  # Circular linkage for the second half

    return head1, head2

