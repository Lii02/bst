class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def __str__(self):
        return f"Root value: {self.root.val}"
    
    def insert(self, val):
        pass