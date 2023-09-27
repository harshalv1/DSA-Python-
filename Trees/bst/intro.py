from collections import deque
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

def level_order(root):

    q=deque()
    q.append(root)
    
    if root is None:
        return 

    while q:
        levels=[]
        for i in range(len(q)):
            node=q.popleft()
            if node:
                levels.append(node.data)
                q.append(node.left)
                q.append(node.right)
        if levels:
            print(levels)               

def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def get_min(root):
    if root is None:
        return None
    curr=root
    while root.left!=None:
        root=root.left

    return root.data

def get_max(root):
    if root is None:
        return None
    curr=root
    while root.right!=None:
        root=root.right

    return root.data



def del_from_bst(root,key):
    if root is None:
        return None
    

    if root.data<key:
        root.right=del_from_bst(root.right,key)
    elif root.data>key:
        root.left=del_from_bst(root.left,key)
    
    else:
        #no child 
        if root.left is None and root.right is None:
            return None
        

        #one child

        if root.right!=None and root.left==None: #right child present left not 
            temp=root.right
            return temp

        elif root.right == None and root.left != None:
            temp=root.left
            return temp
        
        #two child 

        mini=get_min(root.right)
        root.data=mini
        root.right=del_from_bst(root.right,mini)
        return root

    return root 

bst_root=input_dta()
level_order(bst_root)
print("Inorder Traversal:")
inorder(bst_root)

mini=get_min(bst_root)
maxim=get_max(bst_root)
print(end="\n")
print("The minimum element in the bst is",mini)
print("The maximum element in the bst is",maxim)


bst_root=del_from_bst(bst_root,50)
level_order(bst_root)
print("Inorder Traversal:")
inorder(bst_root)
print("\n")

""""
Time complexity is o(h) for deletion because the deletion 
either calls left or right subtree and deletes when the key 
is found . worst case is o(n) for skewed bst
"""

