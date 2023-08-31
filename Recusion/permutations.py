def solve(nums, ans, i):
    # Base case: If the current index i is beyond the length of nums
    if i >= len(nums):
        ans.append(nums[:])  # Add a copy of the current permutation to the result list
        return

    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]  # Make a choice by swapping elements at indices i and j
        solve(nums, ans, i + 1)  # Recursively solve for the next index i + 1
        nums[i], nums[j] = nums[j], nums[i]  # Backtrack by restoring the original order of elements

def permutations(nums):
    ans = []
    i = 0
    solve(nums, ans, i)
    return ans

nums = [1, 2, 3]
res = permutations(nums)
print(res)
