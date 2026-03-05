# A Linked List is a linear data structure where elements are stored in nodes, and each node points to the next node.
# Structure of a node: data + pointer to next node
# Types of Linked Lists: Singly Linked List, Doubly Linked List, Circular Linked List

# Python does not have a built-in Linked List class, so we create manually using classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): #insert at end
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if not current_node:
            return
        prev.next = current_node.next