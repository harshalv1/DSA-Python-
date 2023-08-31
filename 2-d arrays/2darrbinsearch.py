def search(arr_2d, target):
    m = len(arr_2d)
    n = len(arr_2d[0])
    s = 0
    e = m * n - 1
    
    while s <= e:
        mid = s + (e - s) / 2
        
        mid_row = mid // n
        mid_column = mid % n
        
        if arr_2d[mid_row][mid_column] == target:
            return True
        
        elif arr_2d[mid_row][mid_column] > target:
            e = mid - 1
        else:
            s = mid + 1
            
    return False
