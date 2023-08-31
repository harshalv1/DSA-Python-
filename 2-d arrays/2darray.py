

rows=int(input("Rows:"))
columns=int(input("Columns:"))

arr_2d=[] #created an empty array

for i in range(rows):
    row=[] #created an empty list row 
    for j in range(columns):
        value=int(input(f"value to be added at [{i}][{j}]")) #f string that takes an input at every i and j 
        row.append(value) #every value is added to row
    arr_2d.append(row) #every row is added to the array 
    

for row in arr_2d: #for every row in arr_2d 
    for element in row: #for every element in the row 
        print(element,end=" ") #that element is print with a space instead of a newline 
    print() #after every row the next elements are printed on the next line 
        
        