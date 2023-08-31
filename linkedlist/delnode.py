
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

    # Traverse the linked list until the end or the desired position
    while temp.next is not None and count < position - 1:
        temp = temp.next
        count += 1

    # If the position is beyond the current length, add the new node at the tail
    if temp.next is None and count < position - 1:
        tail.next = new_node
        tail = new_node
    else:
        # Insert the new node at the specified position
        new_node.next = temp.next
        temp.next = new_node

    return head, tail


def del_node(head, tail, pos):
    if pos == 1:
        temp = head  # Store the current head node in a temporary variable
        head = head.next  # Update the head to point to the next node
        temp.next = None  # Remove the reference to the original head node
        del temp  # Delete the original head node from memory
        return head, tail  # Return the updated head and tail

    else:
        count = 1  # Initialize the counter variable
        curr = head  # Set curr as the reference to the head node
        prev = None  # Set prev to None initially
        while count < pos:  # Traverse the linked list until the desired position
            prev = curr  # Update the prev reference to point to the current node
            curr = curr.next  # Move curr to the next node
            count = count + 1  # Increment the counter variable

        prev.next = curr.next  # Update the links to bypass the node to be deleted
        curr.next = None  # Remove the reference from the deleted node
        del curr  # Delete the node from memory

        if prev.next is None:  # If the last node is deleted, update the tail
            tail = prev  # Update the tail to point to the previous node

        return head, tail  # Return the updated head and tail


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
    
    # print("Head:", head.data)
    # print("Tail:", tail.data)

    head,tail=del_node(head,tail,4)
    print_list(head)

    print("Head:", head.data)
    print("Tail:", tail.data)

