
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addtohead(head, data):
    # Create a new node with the given data
    new_node = Node(data)
    # Set the next pointer of the new node to the current head
    new_node.next = head
    # Update the head to point to the new node
    head = new_node
    return head

def addtotail(tail, data):
    # Create a new node with the given data
    new_node = Node(data)
    # Set the next pointer of the current tail to the new node
    tail.next = new_node
    # Update the tail to point to the new node
    tail = new_node
    return tail

def addtopos(head, tail, position, data):
    if position == 1:
        return addtohead(head, data)
    new_node = Node(data)
    temp = head
    count = 1
    while count < position - 1:
        temp = temp.next
        count = count + 1
    # Insert the new node at the specified position
    new_node.next = temp.next
    temp.next = new_node 
    if new_node.next is None:
        tail = new_node
    return head, tail

def print_list(head):
    if head is None:
        print("Empty")
        return
    temp = head
    while temp is not None:
        # Print the data of each node
        print(temp.data, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    # Create the initial node
    node1 = Node(2)
    head = node1
    tail = node1
    # Add nodes at various positions
    head = addtohead(head, 1)  # Add 3 at the head
    print_list(head)
    tail = addtotail(tail, 3)  # Add 5 at the tail
    print_list(head)
    head, tail = addtopos(head, tail, 4, 5)  # Add 1 at position 4
    print_list(head)
    
    print("Head:", head.data)
    print("Tail:", tail.data)

    
