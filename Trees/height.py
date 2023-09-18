

def height(root):
    if root is None:
            return 0

    left_depth=height(root.left)
    right_depth=height(root.right)   
    return max(left_depth,right_depth)+1

#time complexity is o(n) because every node is visited only once 
#space complexity in the worst case is o(h) i.e height / o(n) for a skewed binary tree
#this is because s.c in recursion is the maximum depth of the call stack which in the worst
#case for a binary tree is its height
