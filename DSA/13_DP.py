# Dynamic Programming is Optimized Recursion
# It is used to solve problems that can be broken down into smaller overlapping subproblems.
# It uses memoization (top-down) or tabulation (bottom-up) to store results

# e.g. Fibonacci Sequence
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))  # Output: 55

# tabulation approach
def fib_tab(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fib_tab(10))  # Output: 55