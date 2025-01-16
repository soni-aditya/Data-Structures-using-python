'''
Check whether a binary tree is a full binary tree or not


A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes. Conversely, there is no node in a full binary tree, which has one child node. 
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


def isFullTree(root: BinaryTree) -> bool:
    if not root:
        return True

    if not root.left and not root.right:
        return True
    elif root.left is not None and root.right is not None:
        return isFullTree(root.left) and isFullTree(root.right)
    else:
        return False


if __name__ == '__main__':
    tree = BinaryTree(50)

    tree.insert(40)
    tree.insert(60)
    tree.insert(30)
    tree.insert(45)

    print(f"The tree is a full tree: {isFullTree(tree)}")


'''
Time complexity: O(n) where n is number of nodes in given binary tree.
Auxiliary Space: O(n) for call stack since using recursion
'''
