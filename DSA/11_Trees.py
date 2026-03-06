# Trees: A hierarchical data structure consisting of nodes, with one node designated as the root, and the remaining nodes organized in a parent-child relationship.
# Types of Trees: Binary Tree, Binary Search Tree, AVL Tree, Red-Black Tree, B-Tree, Trie

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_traversal(self):
        return self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        res = []
        if node:
            res = self._inorder_helper(node.left)
            res.append(node.data)
            res = res + self._inorder_helper(node.right)
        return res


# DFS Traversal: Inorder (Left, Root, Right), Preorder (Root, Left, Right), Postorder (Left, Right, Root)

def inorder_traversal(root):
    if not root:
        return
    
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

def preorder_traversal(root):
    if not root:
        return
    
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)  

def postorder_traversal(root):
    if not root:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)  
    print(root.data)