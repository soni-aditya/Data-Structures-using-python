'''
Also called level order search/traversal

The best approach is to use a queue
For each node, first, the node is visited and then it’s child nodes are put in a FIFO queue. 


breadth_first_search(tree)
1) Create an empty queue q
2) temp_node = root       /*start from root*/
3) Loop while temp_node is not NULL
    a) print temp_node->data.
    b) Enqueue temp_node’s children 
      (first left then right children) to q
    c) Dequeue a node from q.
'''


class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def breadth_first_search(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        # Print front of queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # add left child to queue
        if node.left is not None:
            queue.append(node.left)

        # add right child to queue
        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.left = BinaryTree(2)
    tree.right = BinaryTree(3)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(5)

    print(f"Bredth first traversal: -")
    breadth_first_search(tree)

'''
Time Complexity: O(n) where n is the number of nodes in the binary tree.
Auxiliary Space: O(n) where n is the number of nodes in the binary tree.
'''
