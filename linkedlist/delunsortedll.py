#del duplicates in an unsorted linked list.

def del_unsorted(head):
    if head==None:
        return None
    
    curr=head
    while curr!=None:
        prev=curr
        temp=curr.next
        while temp!=None:
            if temp.data==curr.data:
                prev.next=temp.next
                
            else:
                prev=temp
            temp=temp.next

        curr=curr.next
    return head 