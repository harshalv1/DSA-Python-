rows=int(input("rows:"))
columns=int(input("columns:"))

arr_2d=[]
sumofrow=0
for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input("What;s the no:"))
        row.append(value)
    arr_2d.append(row)
print("------")
for row in arr_2d:
    for element in row:
        sumofrow=sumofrow+element
    print(sumofrow)
    sumofrow=0

    
        