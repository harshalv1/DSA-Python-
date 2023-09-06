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

# Function to find the largest rectangular area in a histogram
def largest_area(heights):
    n = len(heights)

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

heights = [6, 2, 5, 4, 5, 1, 6]
result = largest_area(heights)
print(result)
