class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)]
                             for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        for row_index, row in enumerate(self.m_adj_matrix):
            print(row)

    def get_transpose_graph(self):
        transpose_graph = [
            [0 for column in range(self.num_of_nodes)]
            for row in range(self.num_of_nodes)
        ]

        for row_index, row in enumerate(self.m_adj_matrix):
            for col_index, col in enumerate(row):
                transpose_graph[col_index][row_index] = col

        for row_index, row in enumerate(transpose_graph):
            print(row)


if __name__ == '__main__':
    graph = Graph(5)

    graph.add_edge(0, 0, 25)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 1)
    graph.add_edge(1, 4, 15)
    graph.add_edge(4, 2, 7)
    graph.add_edge(4, 3, 11)
    print("Graph ------->")
    graph.print_adj_matrix()
    print("Transpose Graph ------->")
    graph.get_transpose_graph()
