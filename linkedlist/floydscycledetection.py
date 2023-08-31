def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def floyd_detect_loop(head):
#     if head is None:
#         return None

#     slow = head
#     fast = head

#     while slow is not None and fast is not None:
#         fast = fast.next
#         if fast is not None:
#             fast = fast.next

#         slow = slow.next

#         if slow == fast:
#             return slow

#     return None


