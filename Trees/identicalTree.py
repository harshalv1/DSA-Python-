'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is not None and root2 is None :
            return False
            
        if root1 is None and root2 is not None :
            return False
        
        
        
        left_side=self.isIdentical(root1.left,root2.left)
        right_side=self.isIdentical(root1.right,root2.right)
        
        value= root1.data==root2.data
        
        
        return left_side and right_side and value
        