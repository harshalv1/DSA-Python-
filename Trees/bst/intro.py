class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        return Node(data)
    
    else:
        if data<root.data:
            root.left=insert(root.left,data)
        else:

            root.right=insert(root.right,data)
    return root
        

def input_dta():
    root=None
    while True:
        data=int(input("What is the node :"))

        if data==-1:
            break
            
        root=insert(root,data)

    return root 


def print_tree(root):
    if root is None:
        return 
    else:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)
    
bst_root=input_dta()
print_tree(bst_root)