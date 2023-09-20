'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    
    def bal_fast(self,root):
        if root is None:
            return True,0
            
        leftans,left_height=self.bal_fast(root.left)
        rightans,right_height=self.bal_fast(root.right)
        
        balanced= leftans and rightans and abs(left_height-right_height)<=1
        
        height=max(left_height,right_height)+1
        
        return balanced ,height
        
        
        
        
    def isBalanced(self,root):
        
        return self.bal_fast(root)[0]
        