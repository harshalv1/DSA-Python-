#49 out of 58 test cases

class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.arr=[0]*k
        self.front=-1
        self.rear=-1

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        
        elif self.isEmpty():
            self.front=self.rear=0
            self.arr[self.rear]=value

        elif self.front!=0 and self.rear==self.size-1:
            self.rear=0
            self.arr[self.rear]=value
        else:
            self.rear+=1
            self.arr[self.rear]=value
        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        ans=self.arr[self.front]

        if self.front==self.rear:
            self.front=self.rear=-1
        
        elif self.front==self.size -1:
            self.front=0
        
        else:
            self.front+=1;
        
        return ans

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1 
        else:
            return self.arr[self.front]        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        else:
            return self.arr[self.rear]
        

    def isEmpty(self) -> bool:

        if self.front==-1:
            return True
        else:
            return False

    def isFull(self) -> bool:

        if :
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()