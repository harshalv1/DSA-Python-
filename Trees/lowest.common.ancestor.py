'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        if root is None:
            return None
        
        if root.data==n1 or root.data==n2:
            return root 
        
        left_ans=self.lca(root.left,n1,n2)

        right_ans=self.lca(root.right,n1,n2)
        
        if left_ans!= None and right_ans!=None:
            return root
        elif left_ans!= None and right_ans==None:
            return left_ans
        elif left_ans== None and right_ans!=None:
            return right_ans
            
        else:
            return None
