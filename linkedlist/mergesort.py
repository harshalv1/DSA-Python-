class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the middle of the linked list
def find_mid(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow 

# Function to merge two sorted linked lists while maintaining order
def solve(first, second):
    curr1 = first
    curr2 = second
    next1 = first.next

    while curr1 != None and curr2 != None:
        if curr2.data > curr1.data and curr2.data < next1.data:
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1

            curr1 = next1
            curr2 = next2
        else:
            curr1 = next1
            next1 = next1.next

            if next1.next == None:
                curr1.next = curr2.next
                break
    return first

# Function to merge two linked lists in sorted order
def merge(first, second):
    if first == None:
        return second
    
    elif second == None:
        return first
    
    if first.data < second.data:
        return solve(first, second)
    else:
        return solve(second, first)

# Function to perform merge sort on a linked list
def merge_sort(head):
    # Base case: empty or single-element list is already sorted
    if head is None or head.next is None:
        return head
    
    # Find the middle of the linked list
    middle = find_mid(head)

    # Divide the linked list into two halves
    left = head
    right = middle.next

    middle.next = None

    # Recursively sort and merge the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    sortedlist_head = merge(left, right)

    return sortedlist_head


#Since the recursive calls form a binary tree of depth log2(n), and each level of the tree takes O(n) time to merge the sublists, the overall time complexity is O(n log n).
#everytime log(n) lists are created coz of the recursive calls hence the space complexity comes out to be log(n)