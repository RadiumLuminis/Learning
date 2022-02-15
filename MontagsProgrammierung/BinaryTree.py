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

# Print the tree
    def PrintTree(self):
        if self.__left:
            self.__left.PrintTree()
        print(self.__data),
        if self.__right:
            self.__right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()