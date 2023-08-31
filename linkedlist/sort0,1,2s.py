##first approach based on counting 0's ,1's  and 2's and then inserting them 
class Node:
     def __init__(self, data):
        self.data = data
        self.next = None

# def sortem(head):
#     # Initialize counters for values 0, 1, and 2
#     zero_count = 0
#     one_count = 0
#     one_count = 0

#     curr = head
#     # Count occurrences of each value in the linked list
#     while curr != None:
#         if curr.data == 0:
#             zero_count = zero_count + 1
#         elif curr.data == 1:
#             one_count = one_count + 1
#         elif curr.data == 2:
#             one_count = one_count + 1
#         curr = curr.next
    
#     curr = head
#     # Update values in the linked list based on the counts
#     while curr != None:
#         if zero_count != 0:
#             curr.data = 0
#             zero_count = zero_count - 1
#         elif one_count != 0:
#             curr.data = 1
#             one_count = one_count - 1
#         elif one_count != 0:
#             curr.data = 2
#             one_count = one_count - 1
#         curr = curr.next
    
#     return head

## Approach:2 create three separate linked lists and add 0 ,1 and 2's separately 
## to them and at the end merge all three lists 


# def insertAtTail(tail, curr):
#     tail.next = curr
#     tail = curr

# def sortlist(head):
#     # Create dummy nodes and tails for three lists
#     zerohead = Node(-1)
#     zerotail = zerohead
#     onehead = Node(-1)
#     onetail = onehead
#     twohead = Node(-1)
#     twotail = twohead

#     curr = head
#     # Traverse the original list and distribute nodes into three lists
#     while curr != None:
#         value = curr.data
#         if value == 0:
#             insertAtTail(zerotail, curr)
#         elif value == 1:
#             insertAtTail(onetail, curr)
#         elif value == 2:
#             insertAtTail(twotail, curr)
#         curr = curr.next

#     # Connect the three lists and form the sorted linked list
#     if zerotail.next != None:
#         zerotail.next = onehead.next
#     else:
#         zerotail.next = twohead.next
#     onetail.next = twohead.next
#     twotail.next = None

#     # Update the head of the sorted linked list
#     head = zerohead.next

#     # Clean up dummy nodes
#     del zerohead
#     del onehead
#     del twohead

#     return head

##--Time Complexity of both approaches is o(n)
##--Space Complexity of both approaches is o(1)