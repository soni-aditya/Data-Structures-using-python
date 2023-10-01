'''
Given a random list of tree nodes, traverse the tree in depth-first pre-order to print out node characters that:
a. One line per node;
b. each node prefixed with “_” according to its level.

The tree node is defined as:
class Node {
int id; // id is non zero
int p_id; // if p_id==0 then this is a root node.
char c;
}

e.g. Node A{5, 6, 'A'}, B{6, 0, "B"},C{4, 6, 'C'}

he explains that here we print "B" first without prefix, and then "A" with one "_",and "C" with one "_"

I suggest using dictionary to save the information in list. And then print it out.
'''

class Node:
    def __init__(self, id, p_id, c):
        self.id = id
        self.p_id = p_id
        self.c = c

# Sample tree nodes
nodes = [
    Node(5, 6, 'A'),
    Node(6, 0, 'B'),
    Node(4, 6, 'C')
]

# Create a dictionary to organize nodes by level
node_dict = {}
for node in nodes:
    level = 0
    current_node = node
    while current_node.p_id != 0:
        level += 1
        current_node = next(n for n in nodes if n.id == current_node.p_id)
    node_dict.setdefault(level, []).append(node)

# Function to print nodes with prefixes based on their levels
def print_tree(node_dict, level=0):
    if level in node_dict:
        for node in node_dict[level]:
            print("_" * level + node.c)
            print_tree(node_dict, level + 1)

# Start printing from the root level
print_tree(node_dict)
