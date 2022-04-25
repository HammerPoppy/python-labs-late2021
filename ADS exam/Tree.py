import collections
import copy


class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = None
        self.insert(data)

    # adds item or any collection of items to Tree
    def insert(self, data):
        # if it is an array adds it's items
        if isinstance(data, collections.abc.Sequence):
            for item in data:
                self.insert(item)
            return

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # removes item from Tree
    def remove(self, data):
        if self is None:
            return self
        if self.data is None:
            return
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data)
            return self
        if data > self.data:
            if self.right:
                self.right = self.right.remove(data)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right

        min_larger_Tree = self.right
        while min_larger_Tree.left:
            min_larger_Tree = min_larger_Tree.left
        self.data = min_larger_Tree.data
        self.right = self.right.remove(min_larger_Tree.data)
        return self

    # deletes all data from Tree
    def disintegrating_directive(self):
        self.left = None
        self.right = None
        self.data = None

    # checks if Tree is empty
    def is_empty(self):
        return (self.data is None) and (self.left is None) and (self.right is None)

    # checks if item is present in Tree
    def has(self, data):
        if data == self.data:
            return True

        if self.data is None:
            return False

        if data < self.data:
            if self.left is None:
                return False
            return self.left.has(data)

        if self.right is None:
            return False
        return self.right.has(data)

    # returns a copy of Tree
    def get_copy(self):
        return copy.deepcopy(self)

    # Left -> Root -> Right
    def get_inorder(self, root):
        res = []
        if root:
            res = self.get_inorder(root.left)
            res.append(root.data)
            res = res + self.get_inorder(root.right)
        return res

    # Root -> Left -> Right
    def get_preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.get_preorder(root.left)
            res = res + self.get_preorder(root.right)
        return res

    # Left -> Right -> Root
    def get_postorder(self, root):
        res = []
        if root:
            res = self.get_postorder(root.left)
            res = res + self.get_postorder(root.right)
            res.append(root.data)
        return res
