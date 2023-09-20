'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:

    def sum_fast(self,root):
        if root is None:
            return True,0
        
        if root.left is None and root.right is None:
            return True,root.data
            
        
        boolleft_side,left_sum=self.sum_fast(root.left)
        boolright_side,right_sum=self.sum_fast(root.right)
        
        # boolleft_side=left_side[0]
        # boolright_side=right_side[0]
        
        # left_sum=left_side[1]
        # right_sum=right_side[1]
        
        condn= root.data==left_sum+right_sum
        
        if boolleft_side and boolright_side and condn:
            return True,left_sum+right_sum+root.data
        else:
            return False,0
    
        
    
    
    def isSumTree(self,root):
        
        return self.sum_fast(root)[0]
        
        
        
        