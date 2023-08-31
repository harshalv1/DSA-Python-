
rows=int(input("No of rows:"))
columns=int(input("No of columns:"))

arr_2d=[]

for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"The value to be inside the 2-d array:[{i}][{j}]"))
        row.append(value)
    arr_2d.append(row)

max_sum=float('-inf')
max_index=-1

for i in range(len(arr_2d)):
    sumofarr=0
    for element in arr_2d[i]:
        sumofarr=sumofarr+element
        if sumofarr>max_sum:
            max_sum=sumofarr
            max_index=i
print("The index of row with the max sum is:", max_index)