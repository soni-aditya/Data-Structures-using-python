'''
given a matrix of 0s and 1s, where 0 represent water and 1 represent land. An island is a land which is surrounded by water from all sides (except for when its touching the boundary of matrix). 

Write a python code to give me the sub matrix containing the island on which I click. Assuming that I will always click on an island, and a row and column of the clicked cell is given as input
'''

def get_island_submatrix(matrix, row, col):
    def dfs(r, c):
        # Check if the current cell is within bounds and is land
        if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == 1:
            # Mark the cell as visited by changing its value to 2
            matrix[r][c] = 2
            # Recursively explore neighboring land cells
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)

    # Start DFS from the clicked cell
    dfs(row, col)

    # Find the bounds of the island
    min_row, max_row, min_col, max_col = len(matrix), 0, len(matrix[0]), 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 2:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                min_col = min(min_col, c)
                max_col = max(max_col, c)

    # Extract the submatrix containing the island
    island_submatrix = [row[min_col:max_col + 1] for row in matrix[min_row:max_row + 1]]

    return island_submatrix

# Example usage:
matrix = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0]
]

row_clicked = 1
col_clicked = 2

island_submatrix = get_island_submatrix(matrix, row_clicked, col_clicked)

# Print the submatrix containing the island
for row in island_submatrix:
    print(row)
