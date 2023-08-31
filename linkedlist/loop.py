class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a new node at the head of the linked list
def insert_head(head, tail, data):
    # Create a new node
    new_node = Node(data)

    # If the list is empty, the new node becomes the head and tail
    if head is None:
        head = new_node
        tail = new_node
    else:
        # Insert the new node at the head
        new_node.next = head
        head = new_node

    return head, tail

# Function to insert a new node at the tail of the linked list
def insert_tail(head, tail, data):
    # Create a new node
    new_node = Node(data)

    if head is None:
        # If the list is empty, the new node becomes the head and tail
        head = new_node
        tail = new_node
    else:
        # Insert the new node at the tail
        tail.next = new_node
        tail = new_node

    return head, tail

# Function to insert a new node at a specified position in the linked list
def add_atpos(head, tail, pos, data):
    # Create a new node
    new_node = Node(data)

    if pos == 1:
        # If the position is 1, insert at the head
        return insert_head(head, tail, data)
    else:
        count = 1
        curr = head
        while count < pos - 1 and curr.next is not None:
            curr = curr.next
            count += 1

        # Insert the new node at the specified position
        new_node.next = curr.next
        curr.next = new_node

        if new_node.next is None:
            # If the new node is added at the end, update the tail
            tail = new_node

    return head, tail

# Function to delete a node at a specified position in the linked list
def del_atpos(head, tail, pos):
    if pos == 1:
        # Delete the node at the head
        temp = head
        head = temp.next
        temp.next = None
        del temp
    else:
        count = 1
        prev = None
        curr = head
        while count < pos and curr.next is not None:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = curr.next
        curr.next = None
        del curr

        if prev.next is None:
            # If the deleted node was the last node, update the tail
            tail = prev

    return head, tail

# Function to print the elements of the linked list
def print_ll(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Function to find the length of the linked list
def lenofll(head):
    length = 0
    temp = head
    while temp is not None:
        temp = temp.next
        length = length + 1
    return length

# Function to detect if there is a loop in the linked list
def detect_loop(head):
    """
    This function detects whether a loop exists in the given linked list.

    Parameters:
        head (Node): The head node of the linked list.

    Returns:
        Node or None: If a loop is detected, it returns the node at which the slow and fast pointers meet (the first node
        within the loop). If no loop is found, it returns None.
    """
    if head is None:
        return None

    # Initialize two pointers: slow and fast
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        # Move the slow pointer one step at a time
        slow = slow.next

        # Move the fast pointer two steps at a time
        fast = fast.next.next

        # If the slow and fast pointers meet, there is a loop in the linked list
        if slow == fast:
            # Return the node where the pointers meet (a node inside the loop)
            return slow

    # If no loop is found, return None
    return None

# Function to get the starting node of the loop in the linked list
def get_start_ofloop(head):
    """
    This function finds the starting node of the loop in the linked list, assuming a loop exists.

    Parameters:
        head (Node): The head node of the linked list.

    Returns:
        Node or None: If a loop is detected, it returns the node where the loop starts. If no loop is found, it returns None.
    """
    if head is None:
        return None 

    # Initialize two pointers: slow and fast
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        # Move the slow pointer one step at a time
        slow = slow.next

        # Move the fast pointer two steps at a time
        fast = fast.next.next

        # If the slow and fast pointers meet, a loop is present
        if slow == fast:
            # Mark the intersecting node where the loop starts
            intersect = slow

            # Reset the slow pointer to the head
            slow = head

            # Move both slow and fast pointers one step at a time until they meet again
            while slow != intersect:
                slow = slow.next
                intersect = intersect.next

            # The node where they meet again is the starting node of the loop
            return slow

    # If no loop is found, return None
    return None

def remove_loop(head):
    if head == None:
        return

    loop_start=get_start_ofloop(head)
    temp=loop_start
    while temp.next!=loop_start:
        temp=temp.next
    
    temp.next=None


# Main function to test the linked list operations
if __name__ == "__main__":
    head = None
    tail = None

    # Insert elements and perform operations
    head, tail = insert_head(head, tail, 10)
    head, tail = insert_tail(head, tail, 12)
    head, tail = insert_tail(head, tail, 15)
    head, tail = add_atpos(head, tail, 4, 22)
    print_ll(head)
    print(f"head is {head.data}")
    print(f"tail is {tail.data}")

    # Creating a loop in the linked list for testing
    tail.next = head.next.next

    # Check if a loop exists in the linked list and find the starting node of the loop
    loop = get_start_ofloop(head)

    if detect_loop(head) is not None:
        print("Loop is Present")
        print(f"It exists at {loop.data}")
    else:
        print("No loop exists")

    remove_loop(head)