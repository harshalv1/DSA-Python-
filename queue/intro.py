from queue import Queue #imported Queue class from queue module 

queue=Queue() # Initialized a queue 

queue.put(8) # pushed elements 
queue.put(9)
queue.put(10)

first_element=queue.get() #popping the first element in queue as queue follows fifo principle
print(first_element)

print(queue.empty()) #returns bool value 
print(queue.qsize()) # qsize function gets us the size of the array 
