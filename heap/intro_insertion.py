
class Heap:
    def __init__(self):
        self.arr=[-1]*1001
        self.size=0


    def insert(self,value):
        self.size+=1
        index=self.size 

        self.arr[index]=value

        while index>1:
            parent=index//2
            if self.arr[index]>self.arr[parent]:
                self.arr[parent],self.arr[index]=self.arr[index],self.arr[parent]

            else:
                return

heap=Heap()
heap.insert(50)
heap.insert(55)
heap.insert(53)
heap.insert(52)
heap.insert(54)

print(heap.arr[1:heap.size+1])

