class Two_Stacks:
    def __init__(self, s):
        # Initialize the Two_Stacks object with a given size 's'
        self.size = s
        self.arr = [0] * s  # Create an array to hold the elements of both stacks
        self.top1 = -1  # Initialize the top pointer for the first stack
        self.top2 = s  # Initialize the top pointer for the second stack at the end of the array

    def push1(self, num):
        # Push an element 'num' onto the first stack
        if self.top2 - self.top1 >= 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = num
        else:
            print("Stack 1 overflow")

    def push2(self, num):
        # Push an element 'num' onto the second stack
        if self.top2 - self.top1 >= 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = num
        else:
            print("Stack 2 overflow")

    def pop1(self):
        # Pop an element from the first stack
        if self.top1 >= 0:
            ans = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return ans
        else:
            return -1  # Return -1 if the first stack is empty

    def pop2(self):
        # Pop an element from the second stack
        if self.top2 < self.size:
            ans = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return ans
        else:
            return -1  # Return -1 if the second stack is empty
