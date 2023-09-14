# Function to check if person 'a' knows person 'b' based on the matrix M.
def knows(M, a, b):
    if M[a][b] == 1:
        return True
    else:
        return False

# Function to find the celeb in the parceleb using a stack-based approach.
def find_celeb(M, n):
    stack = []

    # Step 1: Initialize the stack with all people (indices).
    for i in range(n):
        stack.append(i)

    # Step 2: Compare pairs of people until only one potential celeb remains.
    while len(stack) != 1:
        a = stack.pop()
        b = stack.pop()

        # If 'a' knows 'b', 'a' cannot be the celeb, so push 'b' back onto the stack.
        if knows(M, a, b):
            stack.append(b)
        # Otherwise, push 'a' back onto the stack.
        else:
            stack.append(a)

    # The last person remaining in the stack is the potential celeb.
    ans = stack.pop()

    # Step 3: Verify if the potential celeb meets the criteria.
    zero_count = 0

    # Count the number of zeros in the row of the potential celeb.
    for i in range(n):
        if M[ans][i] == 0:
            zero_count += 1

    # If there are any non-zero values in the row, it's not a celeb.
    if zero_count != n:
        return -1 

    one_count = 0

    # Count the number of ones in the column of the potential celeb.
    for i in range(n):
        if M[i][ans] == 1:
            one_count += 1

    # A celeb should have n-1 ones in their column.
    if one_count != n - 1:
        return -1

    # Return the index of the potential celeb.
    return ans

# Main function to test the code with a sample matrix M and n.
if __name__ == "__main__":
    M = [
        [0, 1, 1],
        [0, 0, 0],
        [1, 1, 0]
    ]
    n = 3
    result = find_celeb(M, n)

    if result != -1:
        print("The celeb is person", result)
    else:
        print("There is no celeb at the .")
