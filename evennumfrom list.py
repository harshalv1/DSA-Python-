


no_of_elements=int(input("How many elements in the list : "))

def insert_element():
  mylist=[]
  for i in range (no_of_elements):
    n=int(input("add element"))
    mylist.append(n)
  
  return mylist

def return_evens(mylist):
  newlist=[]
  for j in range(len(mylist)):
    if mylist[j]%2==0:
        newlist.append([newlist])
        
  
  return newlist
  
  
  