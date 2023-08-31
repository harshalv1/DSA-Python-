class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):  # Iterative approach
    
    # If the list is empty or has only one node, return the head as it is already reversed
    if head == None or head.next == None:
        return head
    else:
        prev = None
        curr = head
        forward = None
        
        # Iterate through the list, reversing the links
        while curr != None:
            forward = curr.next  # Store the next node in the list to avoid losing the reference
            curr.next = prev  # Reverse the link by pointing the current node to the previous node
            prev = curr  # Update the previous node to be the current node
            curr = forward  # Move the current node forward to the next node in the list
        
        return prev  # Return the new head of the reversed list

# Recursive approach for reversing a linked list
# def rev(head, curr, prev): 
#     if curr == None:
#         head = prev
#         return head

#     forward = curr.next
#     head = rev(head, forward, curr)
#     curr.next = prev

# # Recursive function to reverse a linked list
# def reversedll(head):
#     # Initialize current and previous nodes
#     curr = head
#     prev = None
    
#     # Call the recursive function to reverse the list
#     head = rev(head, curr, prev)
#     return head


#Another recursive approach for reversing the linked list
# def recur_reverse(head):
#     if head==None or head.next==None:
#         return head
    
#     reversed_head=recur_reverse(head.next)
#     head.next.next=head
#     head.next=None
#     return reversed_head

# def reversedll(head):
#     return recur_reverse(head)


#Time complexity of the approaches is o(n)
#Space complexity is o(1)