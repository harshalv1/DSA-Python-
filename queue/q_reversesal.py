#using stack to reverse queue 
class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        
        st=[]
        
        while q.qsize()!=0:
            st.append(q.get(0))
            
        while len(st)!=0:
            q.put(st.pop())
            
        
        return q