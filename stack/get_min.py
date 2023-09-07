class MinStack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.s = []
        # Initialize mini as positive infinity; it will store the current minimum element
        self.mini = float('inf')

    def push(self, data):
        if not self.s:  # If the stack is empty (for the first element)
            self.s.append(data)
            self.mini = data  # Set the current minimum to the first element
        else:
            if data < self.mini:
                # To maintain the minimum, push a special value onto the stack
                self.s.append(2 * data - self.mini)
                self.mini = data  # Update the current minimum
            else:
                self.s.append(data)

    def pop(self):
        if not self.s:  # If the stack is empty, return -1 (or handle it according to your use case)
            return -1
        else:
            curr = self.s.pop()  # Pop the top element from the stack
            if curr > self.mini:
                return curr  # If the popped element is greater than the current minimum, return it
            else:
                prev_min = self.mini
                val = 2 * self.mini - curr  # Calculate the previous minimum
                self.mini = val  # Update the current minimum
                return prev_min  # Return the previous minimum

    def top(self):
        if not self.s:  # If the stack is empty, return -1 (or handle it according to your use case)
            return -1
        curr = self.s[-1]  # Get the top element of the stack
        if curr < self.mini:
            return self.mini  # If it's less than the current minimum, return the minimum
        else:
            return curr  # Otherwise, return the top element

    def is_empty(self):
        # Check if the stack is empty and return True or False accordingly
        return not self.s

    def get_min(self):
        if not self.s:  # If the stack is empty, return -1 (or handle it according to your use case)
            return -1
        return self.mini  # Return the current minimum
