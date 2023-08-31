class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve(first, second):
    # If the first list is empty, connect it to the second list and return
    if first.next == None:
        first.next = second
        return first
        
    curr1 = first
    next1 = first.next
    curr2 = second
    next2 = second.next
    
    # Merge the two lists while maintaining order
    while curr1 != None and curr2 != None:
        if curr2.data >= curr1.data and curr2.data <= next1.data:
            curr1.next = curr2
            next2 = curr2.next
            curr2.next = next1
            
            curr1 = next1
            curr2 = next2
        else:
            curr1 = next1
            next1 = next1.next
        
            if next1 == None:
                curr1.next = curr2
                break
    
    return first

def merge_sorted_ll(first, second):
    if first == None:
        return second
        
    elif second == None:
        return first
    
    # Determine the order of the two lists and call the merge function accordingly
    if first.data < second.data:
        return solve(first, second)
    elif second.data < first.data:
        return solve(second, first)
