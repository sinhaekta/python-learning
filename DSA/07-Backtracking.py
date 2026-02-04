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
#number_of_subsets = 2 ** n 

#   generate binary strings of length n
def generate_binary(n):
    result = []

    def backtrack(path):
        if len(path) == n:
            result.append("".join(path))
            return

        path.append('0')
        backtrack(path)
        path.pop()

        path.append('1')
        backtrack(path)
        path.pop()

    backtrack([])
    return result

print("Binary strings:", generate_binary(3))  # ['000', '001', '010', '011', '100', '101', '110', '111']

# permutation
def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result