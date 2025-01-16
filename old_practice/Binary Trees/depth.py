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

# Compute the "max depth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def total_nodes_in_largest_branch(root):
    if root is None:
        return 0

    # computing and comparing depth of each subtree
    l_depth = total_nodes_in_largest_branch(root.left)
    r_depth = total_nodes_in_largest_branch(root.right)

    if l_depth > r_depth:
        return l_depth+1
    else:
        return r_depth+1


def max_depth(root):
    return total_nodes_in_largest_branch(root) - 1


if __name__ == '__main__':
    tree = BinaryTree(50)

    tree.insert(40)
    tree.insert(60)
    tree.insert(30)
    tree.insert(45)
    print(f"The tree is a full tree: {max_depth(tree)}")
    tree.insert(55)
    tree.insert(65)
    print(f"The tree is a full tree: {max_depth(tree)}")


'''
Time Complexity: O(n)

Auxiliary Space: O(n)
'''
