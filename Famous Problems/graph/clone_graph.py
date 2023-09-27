'''
Return a deep copy(clone) of an undirected graph

each node contains a val(int) and its connected edges list (List[Node]) of its neighbors
'''

class Node:
    def __init__(self,val, neighbors) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node')->'Node':
        old_to_new = {}

        def clone(node: 'Node'):
            if node in old_to_new:
                return old_to_new[node]  # we hv already made a clone of this node
            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbour in node.neighbors:
                copy.neighbors.append(clone(neighbour))
            return copy
        return clone(node) if node else None