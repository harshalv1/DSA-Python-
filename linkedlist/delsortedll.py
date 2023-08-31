#del duplicates in a sorted linked list 
def del_sorted(head):
    if head==None:
        return None

    curr=head
    while curr.next!=None:
        if curr.data==curr.next.data :
            next_next=curr.next.next
            nodetodel=curr.next
            del nodetodel
            curr.next=next_next
            
        else:
            curr=curr.next
    return head
            