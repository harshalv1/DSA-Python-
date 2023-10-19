#maxheap using built in queue
import queue

maxheap=queue.PriorityQueue()

maxheap.put(-4) #use of negations to build a maxheap
maxheap.put(-2)
maxheap.put(-5)
maxheap.put(-3)

print("Top element of max-priority queue",-maxheap.queue[0])
print("size of max-priority queue",maxheap.qsize())
print(maxheap.empty())

minheap=queue.PriorityQueue()

minheap.put(4)
minheap.put(2)
minheap.put(5)
minheap.put(3)

print("Top element of min-priority queue",minheap.queue[0])
print("size of min-priority queue",minheap.qsize())
minheap.get() #get is used to get the element but it pops the element from the data structure 
print("size after popping min-priority queue",minheap.qsize())
print(minheap.empty())

