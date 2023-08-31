
class Node:
    def __init__(self,data):
        self.data=data #Node has two attributes data and next
        self.next=None # data is the value inside it and next is the pointer pointer to the next value 
    
def add(head,data): # add function 
    new_node=Node(data) #created a instance called new_node of the class Node 
    new_node.next=head # now the next pointer of the newly created node is the head 
    return new_node # the new head is returne" for future use 

def print_lst(head):
    if head is None:  #condition for when there are no elements in the linkedlist 
        print("emp")
        return
    
    temp=head # temporary pointer which at present points at the head 
    while temp is not None: # condition for reaching the end of the linkedlist
        print(temp.data) 
        temp=temp.next #temp pointer is updated everytime with temp.next pointer


if __name__=="__main__":

    first_node=Node(10) #object creation

    head=first_node #at first both head and tail points towards the first_node
    tail=first_node

    head=add(head,20) #head needs to be updated with the value return from the add function
    print_lst(head) # so that when we print the list the value is added at the start of the list 

   





