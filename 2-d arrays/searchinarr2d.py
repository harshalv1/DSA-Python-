
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

def ispresent(new_arr,target):
    for row in new_arr:
        if target in row:
            return True
    return False

if ispresent(new_arr,8):
    print("Found")
else:
    print("NOtfound")