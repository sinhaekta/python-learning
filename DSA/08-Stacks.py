# LIFO (Last In, First Out) - Stack data structure implementation
# Python doesn’t have a built-in Stack class, so we use list to behave like a stack.
# Use cases Undo/Redo, Expression evaluation, Backtracking algorithms

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item) #append works from end of the list

    def pop(self):
        if not self.is_empty():
            return self.items.pop() #pop works from end of the list
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

# Example usage
# 1. Reverse a string using stack
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str