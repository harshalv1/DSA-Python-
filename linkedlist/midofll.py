#Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.

 
def get_length(head):
    length=0
    temp=head
    while temp is not None:
        temp=temp.next
        length=length+1

    return length

def find_mid(head):
    
    length=get_length(head)
    mid=(length//2)+1
    curr=head
    count=1
    while count<mid:
        curr=curr.next
        count=count+1
    
    return curr

#optimised solution (fast do kadam chalta hai slow ek kadam jab fast last tak pohach jata hai tab slow mid par pohach jata hai)

# def find_mid(head):
#     slow = head
#     fast = head

#     while fast is not None and fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next

#     return slow


#time complexity of the first soln is o(n) and for the second soln is o(n/2) i.e o(n)
# since we get our answer at the mid pos