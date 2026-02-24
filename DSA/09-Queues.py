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

# Circular queue
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            return "Queue is full"
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "Queue is empty"
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        return self.queue[self.front] if self.size > 0 else "Queue is empty"

    def get_size(self):
        return self.size

# Example
#Level order traversal of a binary tree using queue
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None   

    def level_order_traversal(root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(TreeNode.level_order_traversal(root))  # Output: [1, 2, 3, 4, 5]  