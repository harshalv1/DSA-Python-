def solver(digits, output, ans, i, mappings):
    # Base case: when all digits have been considered
    if i >= len(digits):
        ans.append(output)
        return

    num = int(digits[i])
    value = mappings[num]

    # Iterate over each character in the value corresponding to the current digit
    for ch in value:
        # Append the current character to the output and make the recursive call
        solver(digits, output + ch, ans, i + 1, mappings)


def combinations(digits):
    ans = []

    # Base case: empty input
    if len(digits) == 0:
        return ans

    output = ""
    i = 0
    mappings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # Start the recursive backtracking process
    solver(digits, output, ans, i, mappings)

    return ans


# Example usage
digits = "23"
res = combinations(digits)
print(res)
