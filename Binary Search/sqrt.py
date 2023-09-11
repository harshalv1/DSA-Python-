

class Solution:
    def mySqrt(self, x: int) -> int:


        if x==0:
            return 0 
        
        elif x==1:
            return 1 
        
        else:

            s=0
            e=x//2

            while s<=e:
                mid=s+(e-s)//2

                if mid*mid==x:
                    return mid 
                
                elif mid*mid<x:
                    s=mid+1

                else:
                    e=mid-1
                
            return e
