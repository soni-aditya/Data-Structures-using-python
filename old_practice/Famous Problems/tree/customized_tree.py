'''
Design a tree-like data structure with two functionalities:

SetRoot(int nodeId): sets the root of the tree to the given Id node.
IsAncestor(int nodeId1, int nodeId2): return true/false if nodeId1 is ancestor of nodeId2.
Optimize DS for IsAncestor calls. Note that on calls of SetRoot, the connections direction may change.
I was asked to think of better time complexity than O(N), where N is no of nodes
'''

class Tree:
    def __init__(self):
        self.graph = {}  # Directed graph representation
        self.ancestors = {}  # Ancestor data structure

    def SetRoot(self, nodeId):
        # Rebuild the tree rooted at nodeId
        self.graph = {}
        self.ancestors = {}
        self.buildTree(nodeId, None)

    def buildTree(self, currentNode, parent):
        # Recursive function to build the tree
        self.graph[currentNode] = []
        if parent is not None:
            self.graph[currentNode].append(parent)
            self.ancestors[currentNode] = self.ancestors[parent] + [parent]
        else:
            self.ancestors[currentNode] = []

        for child in self.graph[currentNode]:
            self.buildTree(child, currentNode)

    def IsAncestor(self, nodeId1, nodeId2):
        # Check if nodeId1 is an ancestor of nodeId2
        return nodeId1 in self.ancestors[nodeId2]


# Example usage:
tree = Tree()
tree.SetRoot(1)
tree.graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

tree.ancestors = {
    1: [],
    2: [1],
    3: [1],
    4: [1, 2],
    5: [1, 2],
    6: [1, 3]
}

print(tree.IsAncestor(1, 4))  # True
print(tree.IsAncestor(2, 6))  # False
