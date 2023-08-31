def solve(string, output, ans, i):
    # Base case: when all characters have been considered
    if i >= len(string):
        ans.append(output)
        return

    # Exclude the current character
    solve(string, output, ans, i + 1)

    # Include the current character
    output += string[i]
    solve(string, output, ans, i + 1)


def substrings(string):
    output = ""  # Current substring being generated
    ans = []  # List to store all substrings
    i = 0  # Index to keep track of the current character in the string
    solve(string, output, ans, i)  # Start the recursive backtracking process
    return ans


# Example usage
string = "abc"
subs = substrings(string)
print(subs)
