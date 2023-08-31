
def search(arr_2d,target):
    rows=len(arr_2d)
    cols=len(arr_2d[0])
    row_index=0
    col_index=0

    while (row_index<rows and col_index>=0):
        n=arr_2d[row_index][col_index]
        if n==target:
            return True
        elif n<target:
            col_index=col_index-1
        else:
            row_index=row_index+1
    return False