class Two_Stacks:
    def __init__(self,s):
        self.size=s
        self.arr=[0]*s
        self.top1=-1
        self.top2=s
    
    def push1(self,num):
        if self.top2-self.top1>=1:
            self.top1=self.top1+1
            self.arr[self.top1]=num
        else:
            print("stack overflow ")
    
    def push2(self,num):
        if self.top2-self.top1>=1:
            self.top2=self.top2-1
            self.arr[self.top2]=num
        else:
            print("stack overflow")

    def pop1(self):
        if self.top1>=0:
            ans=self.arr[self.top1]
            self.top1=self.top1-1
            return ans 
        else:
            return -1 
    
    def pop2(self):

        if self.top2<self.size:
            ans=self.arr[self.top2]
            self.top2=self.top2+1
            return ans 
        else:
            return -1



            


