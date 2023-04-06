class BST:
    def __init__(self, val, root = None, tab = 0):
        self.val = val
        self.root = root
        self.tab = tab
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val == val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BST(val, self, self.tab + 4)
            return
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BST(val, self, self.tab + 4)
        self.right.root = self

    def get_minimum(self):
        current = self
        while current.left != None:
            current = current.left
        return current.val

    def get_maximum(self):
        current = self
        while current.right != None:
            current = current.right
        return current.val
    
    def delete(self, val):
        if not self:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if not self.right:
            return self.left
        if not self.left:
            return self.right
        min = self.right
        while min.left:
            min = min.left
        self.val = min.val
        self.right = self.right.delete(min.val)
        return self

    def __str__(self):
        output = ""
        for i in range(self.tab):
            output += ' '
        output += f"Value: {self.val}\n"
        if self.left:
            output += f"L {self.left}"
        if self.right:
            output += f"R {self.right}"
        return output