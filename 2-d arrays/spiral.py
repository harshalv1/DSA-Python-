rows=int(input("No of rows:"))
columns=int(input("No of columns:"))

arr_2d=[]

for i in range(rows):
    row=[]
    for j in range(columns):
        value=int(input(f"The value to be inside the 2-d array:[{i}][{j}]"))
        row.append(value)
    arr_2d.append(row)

def spiral(arr_2d,rows,columns):
    count=0 #variable that keeps track of count 
    total=rows*columns #total no of elements in the 2-d array are rows*columns
    
    row_start=0 #index which keeps track of the the start of row  
    row_end=rows-1 # index which keeps track of the the end of the row
    col_start=0 # same for columns 
    col_end=columns-1
    
    spiraled=[] # new array which would store the spiraled elements 
    
    while count<total: #the loop goes on until it has traversed every element 
        for i in range(col_start,col_end+1): #it transverses the start element of every column
            spiraled.append(arr_2d[row_start][i]) #the first row is appended in the spiraled array
            count=count+1 #count is incremented 
        row_start=row_start+1 
        
        for i in range(row_start,row_end+1): #transversed the end element of every row
            spiraled.append(arr_2d[i][col_end]) #the lsat colum is appended in in the spiraled array 
            count=count+1
        col_end=col_end-1
        
        for i in range(col_end,col_start-1,-1): #similar to the above 
            spiraled.append(arr_2d[row_end][i])
            count=count+1
        row_end=row_end-1
        
        for i in range(row_end,row_start-1,-1):
            spiraled.append(arr_2d[i][col_start])
            count=count+1
        col_start=col_start+1
    print(spiraled) 
   
spiral(arr_2d,rows,columns)     