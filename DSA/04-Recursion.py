# Fibonacci Sequence -> 0,1,1,2,3,5,8,13,21,34,55,89,...
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# n! -> 5! = 5*4*3*2*1 = 120
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Sum of first n natural numbers -> 1 + 2 + 3 + ... + n
def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n-1)

# Power function -> x^n
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

# Palindrome check
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])