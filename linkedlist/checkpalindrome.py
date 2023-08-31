class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def checkpalindrome(head):

    values=[]
    curr=head

    while curr!=None:
        values.append(curr.data) 
        curr=curr.next
    
    s=0
    e=len(values)-1

    while s<=e:
        if values[s]!=values[e]:
            return False
        
        s=s+1
        e=e-1
    return True       
    
# Construct the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# Call the function
print(checkpalindrome(head)) 

#Time complexity is o(n)        
#Space complexity is o(n) we want to solve the problem in constant space 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head
    fast = head
    
    # Traverse the list with two pointers: slow moves one step at a time,
    # fast moves two steps at a time. When fast reaches the end, slow will be at the middle.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
        
def reverse(head):
    prev = None
    curr = head
    
    # Reverse the linked list in place by changing the next pointers.
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev
    
  
def check_palindrome(head):
    # Find the middle of the linked list.
    middle = find_middle(head)
    
    # Reverse the second half of the linked list.
    secondhalf_rev = reverse(middle)
    
    # Compare the elements of the first half with the reversed second half.
    first_half = head
    while secondhalf_rev:
        if first_half.data != secondhalf_rev.data:
            return False
        first_half = first_half.next
        secondhalf_rev = secondhalf_rev.next
    return True
