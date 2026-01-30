# All possible combinations, permutations, and subsets

# Generate all subsets
def subsets(nums):
    result = []

    def backtrack(index, path):
        result.append(path[:])  # store a copy

        for i in range(index, len(nums)):
            path.append(nums[i])        # choose
            backtrack(i + 1, path)      # explore
            path.pop()                  # undo (backtrack)

    backtrack(0, [])
    return result

print("Subsets:", subsets([1, 2, 3]))