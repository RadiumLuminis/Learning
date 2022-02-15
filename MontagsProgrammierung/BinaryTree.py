class Node:
    def __init__(self, __data):
        self.__left = None
        self.__right = None
        self.__data = __data

    def insert(self, __data):
# Compare the new value with the parent node
        if self.__data:
            if __data < self.__data:
                if self.__left is None:
                    self.__left = Node(__data)
                else:
                    self.__left.insert(__data)
            elif __data > self.__data:
                if self.__right is None:
                    self.__right = Node(__data)
                else:
                    self.__right.insert(__data)
            else:
                self.__data = __data

# Inorder traversal
# Left -> Root -> Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.__left)
            res.append(root.__data)
            res = res + self.InorderTraversal(root.__right)
        return res

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.__data)
            res = res + self.PreorderTraversal(root.__left)
            res = res + self.PreorderTraversal(root.__right)
        return res

# Postorder traversal
# Left -> Right -> Root 
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.__left)
            res = res + self.PostorderTraversal(root.__right)
            res.append(root.__data)
        return res

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.InorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))