# Import the defaultdict and deque classes from the collections module
from collections import defaultdict, deque

# Create a class named Solution
class Solution:
    # Define a method named FirstNonRepeating that takes a string A as input
    def FirstNonRepeating(self, A):
        # Create a defaultdict to store character counts
        countS = defaultdict(int)
        
        # Create a deque to maintain a queue of characters
        q = deque()
        
        # Initialize an empty string to store the result
        ans = ""

        # Iterate through each character in the input string A
        for ch in A:
            # Increment the count of the current character in countS
            countS[ch] += 1
            
            # Append the current character to the end of the deque q
            q.append(ch) 

            # Check if the deque q is not empty and if the count of the first character in the deque is greater than 1
            while q and countS[q[0]] > 1:
                # Remove the first character from the deque q
                q.popleft()
            
            # If the deque q is not empty, append the first character to the ans string
            if q:
                ans = ans + q[0]
            # If the deque q is empty, append "#" to the ans string
            else:
                ans = ans + "#"
    
        # Return the final ans string containing the first non-repeating characters
        return ans
