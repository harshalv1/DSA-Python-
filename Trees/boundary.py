
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Define a class named 'Solution'
class Solution:
    
    # Helper function to traverse and collect nodes on the left boundary
    def traverseleft(self, root, res):
        # Base case: If the current node is None or is a leaf node, return
        if root is None or (root.left is None and root.right is None):
            return 
        
        # Append the data of the current node to the 'res' list
        res.append(root.data)
        
        # Recursively traverse the left subtree if it exists, otherwise, traverse the right subtree
        if root.left:
            self.traverseleft(root.left, res)
        else:
            self.traverseleft(root.right, res)
    
    # Helper function to traverse and collect leaf nodes
    def traverseleaves(self, root, res):
        # Base case: If the current node is None, return
        if root is None:
            return 
        
        # If the current node is a leaf node, append its data to the 'res' list
        if root.left is None and root.right is None:
            res.append(root.data)
        
        # Recursively traverse both the left and right subtrees
        self.traverseleaves(root.left, res)
        self.traverseleaves(root.right, res)
    
    # Helper function to traverse and collect nodes on the right boundary
    def traverseright(self, root, res):
        # Base case: If the current node is None or is a leaf node, return
        if root is None or (root.left is None and root.right is None):
            return    
        
        # Recursively traverse the right subtree if it exists, otherwise, traverse the left subtree
        if root.right:
            self.traverseright(root.right, res)
        else:
            self.traverseright(root.left, res)
        
        # Append the data of the current node to the 'res' list
        res.append(root.data)

    # Main function to print the boundary view of the binary tree
    def printBoundaryView(self, root):
        # Initialize an empty list 'res' to store the boundary view
        res = []
        # Append the root node's data as the starting point
        res.append(root.data)
        
        # Traverse and collect nodes on the left boundary
        self.traverseleft(root.left, res)
        # Traverse and collect leaf nodes on both left and right subtrees
        self.traverseleaves(root.left, res)
        self.traverseleaves(root.right, res)
        # Traverse and collect nodes on the right boundary
        self.traverseright(root.right, res)
        
        # Return the final boundary view 'res'
        return res
