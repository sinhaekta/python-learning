# A queue is a linear data structure that follows the First In First Out (FIFO) principle.
queue = []

# enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)  # [10, 20, 30]

# dequeue
queue.pop(0) #pop(0) is O(n) because all elements shift left.

print(queue)  # [20, 30]


# Using deque from collections module for efficient queue operations
from collections import deque

queue = deque()

# enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)  # deque([10, 20, 30])

# dequeue
queue.popleft()

print(queue)  # deque([20, 30])

# Class based
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if self.queue else "Queue is empty"

    def size(self):
        return len(self.queue)
