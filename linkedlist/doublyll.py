class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_head(head, tail, data):
    # Create a new node
    new_node = Node(data)
    
    if head == None:
        # If the list is empty, the new node becomes the head and tail
        head = new_node
        tail = new_node
    else:
        # Insert the new node at the head
        new_node.next = head
        new_node.prev = None
        head.prev = new_node
        head = new_node
    
    return new_node, tail

def insert_tail(head, tail, data):
    # Create a new node
    new_node = Node(data)
    
    if tail == None:
        # If the list is empty, the new node becomes the head and tail
        head = new_node
        tail = new_node
    else:
        # Insert the new node at the tail
        tail.next = new_node
        new_node.prev = tail
        new_node.next = None
        tail = new_node
    
    return head, tail

def add_atpos(head, tail, pos, data):
    # Create a new node
    new_node = Node(data)
    
    if pos == 1:
        # If the position is 1, insert at the head
        return insert_head(head, tail, data)
    else:
        count = 1
        curr = head
        while count < pos - 1:
            curr = curr.next
            count += 1
        
        if curr.next == None:
            # If the position is at the end, insert at the tail
            return insert_tail(head, tail, data)
        
        # Insert the new node at the specified position
        new_node.next = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    return head, tail

def del_atpos(head, tail, pos):
    if pos == 1:
        # Delete the node at the head
        temp = head
        temp.next.prev = None
        head = temp.next
        temp.next = None
        del temp
    else:
        count = 1
        prev = None
        curr = head
        while count < pos:
            prev = curr
            curr = curr.next
            count += 1
        
        prev.next = curr.next
        curr.next = None
        curr.prev = None
        del curr
        
        if prev.next == None:
            # Update the tail if the deleted node was the last node
            tail = prev
    
    return head, tail

def print_dll(head):
    # Traverse and print the elements of the doubly linked list
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def lenofdll(head):
    len=0
    temp=head
    while temp is not None:
        temp=temp.next
        len=len+1
    return len

if __name__ == "__main__":
    head = None
    tail = None

    # Insert elements and perform operations
    head, tail = insert_head(head, tail, 3)
    print_dll(head)
    head, tail = insert_tail(head, tail, 5)
    print_dll(head)
    head, tail = insert_head(head, tail, 1)
    print_dll(head)
    head, tail = add_atpos(head, tail, 3, 8)
    print_dll(head)
    head, tail = del_atpos(head, tail, 1)
    print_dll(head)
    print(f"head is {head.data}")
    print(f"tail is {tail.data}")
    #print("lengthofdll :",lenofdll(head))