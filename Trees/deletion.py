from requests import delete


# reference: https://www.youtube.com/watch?v=wMyWHO9F1OM
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


def delete_node_from_BST(current_node: BinaryTree, value: int) -> BinaryTree:
    if not current_node:
        return

    if current_node.data > value:
        # means that our key is to the left of this node
        current_node.left = delete_node_from_BST(current_node.left, value)

    elif current_node.data < value:
        # means that our key is to the right of this node
        current_node.right = delete_node_from_BST(current_node.right, value)

    else:
        # we found the key we want to delete
        '''
        In this case there are 4 possibilities:
            1. there are no children to the node we wanna delete
            2. there is a left child to the node we wanna delete
            3. there is a right child to the node we wanna delete
            4. there are both left and right children to the node we wanna delete
        '''
        if not current_node.left and not current_node.right:
            # we will return none to replace this node with None value to where it was attached
            return None
        elif not current_node.left and current_node.right:
            return current_node.right
        elif current_node.left and not current_node.right:
            return current_node.left
        else:
            # in this case we'll just replace the leftmost value
            # in the right subtree of current_node with the current node itself
            pointer = current_node.right

            while pointer.left:
                pointer = pointer.left

            current_node.data = pointer.data
            # now removing the leftmost node from right subtree of current_node
            # since its value is already copied in place of current_node
            current_node.right = delete_node_from_BST(
                current_node.right, current_node.data)

    return current_node


if __name__ == '__main__':
    tree = BinaryTree(27)

    tree.insert(14)
    tree.insert(35)
    tree.insert(10)
    tree.insert(12)
    tree.insert(19)
    tree.insert(31)
    tree.insert(42)
    print(f"Before deletion: {tree.inorder_traversal(tree)}")
    tree = delete_node_from_BST(tree, 10)
    print(f"After deletion: {tree.inorder_traversal(tree)}")

    # time complexity: height(h) of the tree ie. O(h)
