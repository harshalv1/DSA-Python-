class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_doubly_linked_list(head):
    # Check if the list is empty
    if head is None:
        # If it is empty, return the 'head' as it is
        return head

    # Rest of the reversal code follows...
    current = head
    previous = None

    while current is not None:
        next_node = current.next
        current.next = previous
        current.prev = next_node
        previous = current
        current = next_node

    head = previous

    return head


