'''
Given a binary tree and a node, write a program to find inorder successor of this node.

Inorder Successor of a node in binary tree is the next node in Inorder traversal of the Binary Tree. Inorder Successor is NULL for the last node in Inorder traversal.

We need to take care of 3 cases for any node to find its inorder successor as described below:  

1) Right child of node is not NULL. If the right child of the node is not NULL then the inorder successor of this node will be the leftmost node in it’s right subtree.
2) Right Child of the node is NULL. If the right child of node is NULL. Then we keep finding the parent of the given node x, say p such that p->left = x
3) If node is the rightmost node. If the node is the rightmost node in the given tree. In this case, there will be no inorder successor of this node. i.e. Inorder Successor of the rightmost node in a tree is NULL.
'''


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftMostNode(node):
    # function to find left most node in a tree

    while (node != None and node.left != None):
        node = node.left
    return node


def rightMostNode(node):
    # function to find right most node in a tree

    while (node != None and node.right != None):
        node = node.right
    return node


def findInorderRecursive(root, x):
    # recursive function to find the Inorder Successor
    # when the right child of node x is None
    if (not root):
        return None
    if (root == x or (findInorderRecursive(root.left, x)) or
                     (findInorderRecursive(root.right, x))):
        if findInorderRecursive(root.right, x):
            temp = findInorderRecursive(root.right, x)
        else:
            temp = findInorderRecursive(root.left, x)
        if (temp):

            if (root.left == temp):

                print("Inorder Successor of",
                      x.data, end="")
                print(" is", root.data)
                return None
        return root
    return None

# function to find inorder successor
# of a node


def inorderSuccessor(root, x):

    # Case1: If right child is not None
    if (x.right != None):
        inorderSucc = leftMostNode(x.right)
        print("Inorder Successor of", x.data,
              "is", end=" ")
        print(inorderSucc.data)

    # Case2: If right child is None
    if (x.right == None):
        f = 0
        rightMost = rightMostNode(root)

        # case3: If x is the right most node
        if (rightMost == x):
            print("No inorder successor!",
                  "Right most node.")
        else:
            findInorderRecursive(root, x)


if __name__ == '__main__':

    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)

    # Case 1
    inorderSuccessor(root, root.right)

    # case 2
    inorderSuccessor(root, root.left.left)

    # case 3
    inorderSuccessor(root, root.right.right)


'''
Time Complexity: O( n ), where n is the number of nodes in the tree. 

Space complexity: O(n) for call stack  
'''
