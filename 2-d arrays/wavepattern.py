
rows=int(input("No of rows:"))
columns=int(input("No of columns:"))

arr_2d=[]

for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"The value to be inside the 2-d array:[{i}][{j}]"))
        row.append(value)
    arr_2d.append(row)

for j in range(columns):
    if j%2==0: #when the column in even 
        for i in range(rows): #then print downward
            print(arr_2d[i][j])
    else: #when column is odd 
        for i in range(rows-1,-1,-1): # then print upward in a reverse manner row-1 is the starting index which is last index (inclusive) and -1 is the last index which is exclusive means it goes only till the 0th index and the last -1 means the decrement by -1 
            print(arr_2d[i][j]) 

#every element is traversed once and the total no of elements is n*m so the time complexity is o(nm)