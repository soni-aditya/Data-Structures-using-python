# A class that represents an individual node
# in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # The recur on right child
        printPostorder(root.right)
 
        # Now print the data of node
        print(root.val, end=" "),
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
 
    # Function call
    print("Postorder traversal of binary tree is")
    printPostorder(root)