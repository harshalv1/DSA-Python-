

class Node:
    def __init__(self,data): #constructor having attributes data and left right                     
        self.data=data #as None
        self.left=None 
        self.right=None

def build_tree():
    data=int(input("DAt:")) #take input 

    if data==-1: # if the value is -1 (base case)
        return None
    
    root=Node(data) #construct node with the given value 

    print("Dat at left of",data) 
    root.left=build_tree() #build left subtree using recurstion 

    print("Dat at right of",data)
    root.rigt=build_tree() #build right subtree using recursion 

    return root #return root 

root=build_tree() #function call 


    

