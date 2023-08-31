
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

def insertNode(tail,element,data):
    #if the list is empty
    if tail==None:
        new_node=Node(data) #create new node 
        tail=new_node # assign the new node as the tail 
        new_node.next=new_node # make it point itself 
    
    else:

        curr=tail
        # we search until we can find the element 
        while curr.data!=element:
            curr=curr.next
        
        new_node=Node(data) # create a new node 
        new_node.next=curr.next # make the new node point the tail/curr node which was previously pointing itself 
        curr.next=new_node # make the next pointer of the curr pointer to the newly created node so that the connection is secure 

    return tail  

def del_node(tail,val):
    if tail==None:
        print("SRy list is empty check again")
    else:
        prev=tail
        curr=prev.next

        while curr.data!=val:
            prev=curr
            curr=curr.next

        if curr==prev:
            tail=None
        elif tail== curr:
            tail=prev

        prev.next=curr.next
        curr.next=None
        del curr

    return tail      
  
def iscircular(head):

    if head==None:
        return True

    temp=head.next 
    while temp!=None and temp!=head:
        temp=temp.next

    if temp==head:
        return True

    return False

def printcll(tail):

    if tail==None:
        print("empty list")
    else:
        temp=tail

        while True:
            print(temp.data,end=" ")
            temp=temp.next

            if temp==tail:
                break
        print()
        

if __name__=="__main__":

    tail=None
    tail=insertNode(tail,5,3)
    printcll(tail)
    tail=insertNode(tail,3,8)
    printcll(tail)
    # tail=insertNode(tail,8,11)
    # printcll(tail)
    # tail=insertNode(tail,3,7)
    # printcll(tail)
    # tail=insertNode(tail,8,9)
    # printcll(tail)

    tail=del_node(tail,8)
    #printcll(tail)

    if iscircular(tail):
        print("linked list is cicular in nature ")
    
    else:
        print("linked list is not circular")
    

