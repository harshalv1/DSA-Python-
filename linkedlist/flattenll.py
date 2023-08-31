class Node:
    def __init__(self, data):
        self.data = data
        self.right = None  # Pointer to the next node in the same level
        self.down = None   # Pointer to the node in the next level

# Merges two linked lists in a down-ward manner
def solve(first, second):
    dummy = Node(None)  # Create a dummy node to build the merged list
    curr = dummy        # Pointer to track the current position in the merged list

    while first and second:
        if first.data < second.data:
            curr.down = first
            first = first.down
        else:
            curr.down = second
            second = second.down
        curr = curr.down
    
    # Append remaining nodes if any
    if first == None:
        curr.down = second
    else:
        curr.down = first

    return dummy.down  # Return the merged list

# Merges two sorted linked lists using solve function
def merge_sorted(first, second):
    if first is None:
        return second
    elif second is None:
        return first 
    
    if first.data < second.data:
        return solve(first, second)
    else:
        return solve(second, first)

# Recursively flattens a nested linked list
def flatten(head):
    if head is None or head.down is None:
        return head

    head.right = flatten(head.right)  # Flatten the right side
    flattened_head = merge_sorted(head, head.right)  # Merge current level with flattened right side

    return flattened_head

# Test case
if __name__ == "__main__":
    # Creating the nested linked list
    head = Node(5)
    head.down = Node(7)
    head.down.down = Node(8)
    head.down.down.down = Node(30)

    head.right = Node(10)
    head.right.down = Node(20)

    head.right.right = Node(19)
    head.right.right.down = Node(22)
    head.right.right.down.down = Node(50)

    head.right.right.right = Node(28)
    head.right.right.right.down = Node(35)
    head.right.right.right.down.down = Node(40)
    head.right.right.right.down.down.down = Node(45)

    # Flatten the linked list
    flattened_head = flatten(head)

    # Print the flattened linked list
    temp = flattened_head
    while temp:
        print(temp.data, end=" ")
        temp = temp.down
