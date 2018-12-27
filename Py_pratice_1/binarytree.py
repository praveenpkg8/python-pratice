class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, search):
        if search < self.data:
            if self.left is None:
                return str(search) + " Not Found"
            return self.left.findval(search)
        elif search > self.data:
            if self.right is None:
                return str(search) + " NotFound"
            return self.right.findval(search)
        else:
            print(str(self.data) + " Found")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data,end=" ")
        if self.right:
            self.right.PrintTree()


root = Node(10)
root.insert(6)
root.insert(11)
root.insert(21)
root.insert(3)
root.insert(1)
root.insert(5)s
root.PrintTree()
print(root.findval(3))
print(root.findval(33))


#
# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data
#
#     # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
#
# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
#
# root.PrintTree()
