
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def kreverse(head,k):
    if head==None:
        return None
    
    curr=head
    prev=None
    next_part=None

    count=0
    while curr!=None and count<k:
        next_part=curr.next
        curr.next=prev
        prev=curr
        curr=next_part
        count=count+1
    
    if next_part!=None:
        head.next=kreverse(next_part,k)
    
    return prev
        
