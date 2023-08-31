# arr_2d=[[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(arr_2d)):
#     for j in range(i+1,len(arr_2d)):
#         arr_2d[i][j],arr_2d[j][i]=arr_2d[j][i],arr_2d[i][j]
  
# for i in range(len(arr_2d)):
#     arr_2d[i]=arr_2d[i][::-1]

# for row in arr_2d:
#     print(row)

rows=int(input("rows:"))
columns=int(input("columns:"))

arr_2d=[]
sumofrow=0
for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"What;s the no at [{i}][{j}] :"))
        row.append(value)
    arr_2d.append(row)

for i in range(len(arr_2d)):
    for j in range(i+1,len(arr_2d)):
        arr_2d[i][j],arr_2d[j][i]=arr_2d[j][i],arr_2d[i][j]
        

for i in range(len(arr_2d)):
    arr_2d[i]=arr_2d[i][::-1]

for row in arr_2d:
    print(row)