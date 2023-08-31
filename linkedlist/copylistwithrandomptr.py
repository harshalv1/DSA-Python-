class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb = None

#Approach of mapping uses o(n) space 
def copylist(head):
    if head is None:
        return None
        
    mapping = {}
        
    curr = head
    while curr:
        mapping[curr] = Node(curr.data)
        curr = curr.next
    
    curr = head
    while curr:
        if curr.next:
            mapping[curr].next = mapping[curr.next]
            
        if curr.arb:
            mapping[curr].arb = mapping[curr.arb]
            
        curr = curr.next
        
    return mapping[head]

#approach two: weaving links 
class Solution:
    def copy_list(self, head: 'Node') -> 'Node':
        
        # Helper function to insert a new node at the tail
        def insert_at_tail(head, tail, data):
            new_node = Node(data)
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            return head, tail
        
        # Step 1: Create a clone of the original list
        clone_head = None
        clone_tail = None
        temp = head
        while temp:
            clone_head, clone_tail = insert_at_tail(clone_head, clone_tail, temp.data)
            temp = temp.next
        
        # Step 2: Interweave the original and clone lists
        original_node = head
        clone_node = clone_head
        while original_node:
            next_original = original_node.next
            original_node.next = clone_node
            original_node = next_original
            
            next_clone = clone_node.next
            clone_node.next = original_node
            clone_node = next_clone
        
        # Step 3: Copy random pointers for the clone
        original_node = head
        clone_node = clone_head
        while original_node:
            if original_node.arb:
                clone_node.arb = original_node.arb.next
            else:
                clone_node.arb = None
            original_node = original_node.next
            clone_node = clone_node.next
        
        # Step 4: Separate the original and clone lists
        original_node = head
        clone_node=clone_head
        while original_node:
            original_node=original_node.next.next if original_node.next else original_node
            clone_node=clone_node.next.next if clone_node.next else clone_node.next
            original_node = original_node.next
            clone_node=clone_node.next
            
        # Return the clone list
        return clone_head
