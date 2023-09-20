from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None :
            return None 
        q=deque()
        q.append(root)
        ans=[]
        right2left=True

        while q :
            lev=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    lev.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if right2left:
                ans.append(lev)
                right2left=False
            else:
                ans.append(lev[::-1])
                right2left=True

        return ans

                