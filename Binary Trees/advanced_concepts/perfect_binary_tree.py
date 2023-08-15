'''
Check whether a given binary tree is perfect or not

A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level
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


'''
find_depth----
    This function tests if a binary tree
    is perfect or not. It basically checks
    for two things :
    1) All leaves are at same level
    2) All internal nodes have two children
'''


def find_depth(root: BinaryTree) -> int:
    depth = 0

    while root is not None:
        depth += 1
        # since we are assuming that tree is perfect
        # all leaves will be at the same level
        root = root.left
    return depth


def is_perfect_tree(root: BinaryTree, depth: int, level=0) -> bool:
    if root is None:
        return True

    # if leaf node, then its depth must be equal to the depth of all other leaves
    if root.left is None and root.right is None:
        return depth == level+1

    # if internal node and one child is empty
    if root.left is None or root.right is None:
        return False
    else:
        return is_perfect_tree(root.left, depth, level+1) and is_perfect_tree(root.right, depth, level+1)


def find_if_perfect(root):
    depth = find_depth(root)
    return is_perfect_tree(root, depth)


if __name__ == '__main__':
    tree = BinaryTree(50)

    tree.insert(40)
    tree.insert(60)
    tree.insert(30)
    tree.insert(45)
    print(f"The tree is a full tree: {find_if_perfect(tree)}")
    tree.insert(55)
    tree.insert(65)
    print(f"The tree is a full tree: {find_if_perfect(tree)}")
