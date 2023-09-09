#implementation of cicular queue 
class MyCircularQueue:

    def __init__(self, k: int):

        self.size=k
        self.arr=[0]*k
        self.front=-1
        self.rear=-1


    def enQueue(self, value: int) -> bool:

        if self.front==-1: # when the queue is empty 
            self.front=self.rear=0 #they need to be initialized to the beginning 
            self.arr[self.rear]=value #value is added 
        
        elif self.front!=0 and self.rear==self.size-1 or self.rear==(self.front-1)%(self.size-1): #modulo condition is for wrapping around and the entire condition is for queue is full
            return False
        
        elif self.front!=0 and self.rear==self.size-1: #when front is not at the beginning and rear is at the end 
            self.rear=0 #so it needs to come to beginning to maintain cyclic nature of the queue 
            self.arr[self.rear]=value
        
        else:
            self.rear+=1 #normal push in queue
            self.arr[self.rear]=value

        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        
        element=self.arr[self.front] #element is stored 
        
        if self.front==self.rear: # if we are currently on the first and only element 
            self.front=self.rear=-1 #after popping the queue is empty 

        elif self.front==self.size-1: #if we are at the end 
            self.front=0 # we go to the beginning to maintain cyclic nature 
        
        self.front=self.front+1 #normal flow 

        return element



        

    def Front(self) -> int:
        if self.isEmpty(self):
            return -1
        
        return self.arr[self.front]
        

    def Rear(self) -> int:

        if self.isEmpty(self):
            return -1
        
        return self.arr[self.rear]

    
    def isEmpty(self) -> bool:
        if self.front==-1 and self.rear==-1:
            return True
        else:
            return False
        

    def isFull(self) -> bool:

        if self.front!=0 and self.rear==self.size-1:
            return True
            
        if self.rear==(self.front-1)%(self.size-1):
            return True

        else:
            return False
        