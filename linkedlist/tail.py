

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

def addtohead(head,data):
    new_node=Node(data)
    new_node.next=head
    head = new_node
    return head


def addtotail(tail,data):
    new_node=Node(data) #create a new instance of the class 
    tail.next=new_node #when trying to connect the new node the end the next pointer would point to then new node 
    tail=new_node # and value of tail will be updated with new_node 
    return tail #return the value of tail to be used in the main file / for further use 
     
def print_list(head):
    
    if head is None:
        print("emp")
        return
    temp=head
    while temp is not None:
        print(temp.data,end=" ")
        temp=temp.next
    print()

if __name__=="__main__":
    
    node1=Node(3)
    head=node1
    tail=node1

    head=addtohead(head,2)
    print_list(head)

    tail=addtotail(tail,5)
    print_list(head)
