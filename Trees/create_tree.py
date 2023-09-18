

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
    root.right=build_tree() #build right subtree using recursion 

    return root #return root 

root=build_tree() #function call 

def count(root):
    if root==None:
        return 0

    else:
        return 1+count(root.left)+count(root.right)
    
def inorder (root): #depth first search types inorder preorder and postorder 
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        



# no_of_nodes=count(root)
# print(no_of_nodes)
#inorder(root)
#preorder(root)
postorder(root)

    

