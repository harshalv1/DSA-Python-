
arr_2d=[1,3,4,5,8,7,9,8]
new_arr=[]

rows=2
columns=4

index=0
for i in range(rows):
    row=[]
    for j in range(columns):
        row.append(arr_2d[index])
        index=index+1
    new_arr.append(row)
    
for row in new_arr:
    for element in row:
        print(element,end=" ")
    print()