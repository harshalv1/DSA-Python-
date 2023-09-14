from typing import List
from collections import deque

class Solution:
    def rearrangeQueue(self, N : int, q : List[int]) -> List[int]:
        
        stack=[]
        q=deque(q)
        
        mid=N//2
        
        for i in range(mid):
            val=q.popleft()
            stack.append(val)
        
        while stack:
            val=stack.pop()
            q.append(val)
            
        for i in range(mid):
            val=q.popleft()
            q.append(val)
            
        for i in range(mid):
            val=q.popleft()
            stack.append(val)
            
        while stack:
            q.append(stack.pop())
            val=q.popleft()
            q.append(val)
            
            
        return list(q)
        
    #Time and space complexity are o(n)