'''
determine if a binary tree is height-balanced?

To check if a tree is height-balanced, get the height of left and right subtrees. Return true if difference between heights is not more than 1 and left and right subtrees are balanced, otherwise return false. 
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


def total_nodes_in_largest_branch(root):
    if root is None:
        return 0

    l_height = total_nodes_in_largest_branch(root.left)
    r_height = total_nodes_in_largest_branch(root.right)

    return max(l_height, r_height) + 1


def get_height(root):
    return total_nodes_in_largest_branch(root) - 1


def check_if_height_balanced(root):
    if root is None:
        return True

    l_height = get_height(root.left)
    r_height = get_height(root.right)

    if (abs(l_height - r_height) <= 1) and (check_if_height_balanced(root.left) and check_if_height_balanced(root.right)):
        return True

    return False


if __name__ == '__main__':
    tree = BinaryTree(50)

    tree.insert(40)
    tree.insert(60)
    tree.insert(30)
    tree.insert(45)
    tree.insert(55)
    tree.insert(65)
    print(f"The tree is a full tree: {check_if_height_balanced(tree)}")

'''
Time Complexity: O(n^2) in case of full binary tree.

Auxiliary Space: O(n) space for call stack since using recursion
'''
