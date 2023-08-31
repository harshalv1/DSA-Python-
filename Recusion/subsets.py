class Solution:
    def solve(self, nums, output, index, ans):
        # Base case: when all elements have been considered
        if index >= len(nums):
            ans.append(output.copy())  # Append a copy of the current output to the answer list
            return

        # Exclude the current element
        self.solve(nums, output, index + 1, ans)

        # Include the current element
        element = nums[index]
        output.append(element)  # Add the current element to the output list
        self.solve(nums, output, index + 1, ans)

        output.pop()  # Backtrack: remove the last added element from the output list

    def subsets(self, nums):
        ans = []  # List to store all the subsets
        output = []  # Current subset being generated
        index = 0  # Index to keep track of the current element in nums
        self.solve(nums, output, index, ans)  # Start the recursive backtracking process
        return ans


nums = [1, 2, 3]
sol = Solution()
res = sol.subsets(nums)
print(res)
