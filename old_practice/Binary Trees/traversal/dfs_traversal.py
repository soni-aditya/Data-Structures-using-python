'''
Depth First Traversals
 - Inorder Traversal (Left-Root-Right)
 - Preorder Traversal (Root-Left-Right)
 - Postorder Traversal (Left-Right-Root)
'''


class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)

    def inorder_traversal(self, node):
        if not node:
            return []
        res = []

        res = self.inorder_traversal(node.left)
        res.append(node.data)
        res = res + self.inorder_traversal(node.right)

        return res

    def preorder_traversal(self, node):
        if not node:
            return []
        res = []

        res.append(node.data)
        res = res + self.preorder_traversal(node.left)
        res = res + self.preorder_traversal(node.right)

        return res

    def postorder_traversal(self, node):
        if not node:
            return []
        res = []

        res = self.postorder_traversal(node.left)
        res = res + self.postorder_traversal(node.right)
        res.append(node.data)

        return res


if __name__ == '__main__':
    tree = BinaryTree(27)

    tree.insert(14)
    tree.insert(35)
    tree.insert(10)
    tree.insert(10)
    tree.insert(19)
    tree.insert(31)
    tree.insert(42)
    print(f"Inorder: {tree.inorder_traversal(tree)}")
    print(f"Preorder: {tree.preorder_traversal(tree)}")
    print(f"Postorder: {tree.postorder_traversal(tree)}")

'''
Time Complexity: O(n) 
Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree. 



Complexity function T(n) — for all problems where DFS tree traversal is involved — can be defined as:
T(n) = T(k) + T(n – k – 1) + c
Where k is the number of nodes on one side of the root and n-k-1 on the other side.
'''
