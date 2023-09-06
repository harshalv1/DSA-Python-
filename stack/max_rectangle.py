
# Function to find the next smallest element to the right of each element
def next_smallest_element(arr, n):
    st = [-1]  # Initialize a stack with -1 as a sentinel value
    ans = [0] * n  # Initialize the answer array with zeros

    # Iterate through the elements in reverse order
    for i in range(len(arr) - 1, -1, -1):
        curr = arr[i]
        while st[-1] != -1 and arr[st[-1]] >= curr:
            st.pop()  # Pop elements from the stack until we find a smaller element
        ans[i] = st[-1]  # Store the index of the next smaller element

        st.append(i)  # Push the current element's index onto the stack

    return ans

# Function to find the previous smallest element to the left of each element
def prev_smallest_element(arr, n):
    st = [-1]  # Initialize a stack with -1 as a sentinel value
    ans = [0] * n  # Initialize the answer array with zeros

    # Iterate through the elements
    for i in range(len(arr)):
        curr = arr[i]
        while st[-1] != -1 and arr[st[-1]] >= curr:
            st.pop()  # Pop elements from the stack until we find a smaller element
        ans[i] = st[-1]  # Store the index of the previous smaller element

        st.append(i)  # Push the current element's index onto the stack

    return ans

# Optimised approach time complexity is o(n) the function finds the largest rectangular area in a histogram
def largest_area(heights,n):
    

    # Find the next and previous smaller elements for each element
    next_smaller = next_smallest_element(heights, n)
    prev_smaller = prev_smallest_element(heights, n)

    area = 0  # Initialize the maximum area to zero
    for i in range(n):
        l = heights[i]
        if next_smaller[i] == -1:
            next_smaller[i] = n

        b = next_smaller[i] - prev_smaller[i] - 1  # Calculate the width of the rectangle
        new_area = l * b  # Calculate the area of the rectangle

        area = max(area, new_area)  # Update the maximum area if a larger rectangle is found

    return area

def max_area(M, n, m):
    # Calculate the maximum area of a rectangular submatrix formed by 1s in the given binary matrix M.
    
    # Calculate the maximum area of the first row to initialize the 'area' variable.
    area = largest_area(M[0], m)
    

    # Iterate through the remaining rows in the matrix
    for i in range(1, n):
        for j in range(m):
            if M[i][j] != 0:
                M[i][j] = M[i-1][j] + M[i][j]  # Update the value in the matrix to represent the cumulative height of 1s
            else:
                M[i][j] = 0

        # Calculate the maximum area for the current row and update 'area' if a larger area is found.
        iter_area = largest_area(M[i], m)
        area = max(area, iter_area)

    return area  # Return the maximum area of the rectangular submatrix

# Define a test matrix
matrix1 = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

matrix2 = [
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0]
]

matrix3 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

# Call the max_area function with the test matrix
result1 = max_area(matrix1, len(matrix1), len(matrix1[0]))
result2 = max_area(matrix2, len(matrix2), len(matrix2[0]))
result3 = max_area(matrix3, len(matrix3), len(matrix3[0]))


# Print the results
print("Max Area in matrix1:", result1)
print("Max Area in matrix2:", result2)
print("Max Area in matrix3:", result3)

#time complexity for the code is o(n*m)
#space complexity is o(m)
