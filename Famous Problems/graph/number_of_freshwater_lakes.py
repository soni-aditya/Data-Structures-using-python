"""
Given an input matrix like this

input =
{{0,0,1,0,0,0,0,1,0,0,0,0,0}, 
{0,0,0,0,0,0,0,1,1,1,0,0,0}, 
{0,1,1,1,1,0,0,0,0,0,0,0,0},
{0,1,0,0,1,1,0,0,1,1,1,0,0},
{0,1,0,1,1,1,0,0,1,1,1,0,0},
{0,0,1,0,0,0,0,0,1,0,1,0,0},
{0,0,0,0,0,0,0,1,1,1,0,0,0},
{0,0,0,0,0,0,0,1,1,0,0,0,0}}

Here 0 indidates water and its value can be either saltwater or freshwater
1 is land

the input matrix is implicitly surrounded by an infinite ocean as shown in the comments part in the first and second row.

Here the condition is water moves vertically and horizontally (up down left right) but not diagonally
Write a method which takes this input matrix and return the total number of freshwater lakes. For the above matrix there are two freshwater island.
"""
# considering same number diagonal direction as 1 connect

from collections import deque

def fill_sea(grid):
    visited = set()
    rows,cols = len(grid), len(grid[0])
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
    def BFS(r, c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                dr,dc = row+dr, col+dc
                
                if (dr>=0 and dr<rows) and (dc>=0 and dc<cols) and (grid[dr][dc]==0) and ((dr,dc) not in visited):
                    visited.add((dr,dc))
                    q.append((dr,dc))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row==0 or row==len(grid)-1) and (row,col) not in visited and grid[row][col]==0:
                BFS(row,col)
            elif col ==0 or col == len(grid[row])-1 and (row,col) not in visited and grid[row][col]==0:
                BFS(row,col)
    
    for row,col in visited:
        grid[row][col] = 1
    return grid

def count_lakes(grid):
    grid = fill_sea(grid)
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
    visited = set()
    rows,cols = len(grid), len(grid[0])

    def BFS(r, c):
        q = deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                dr,dc = row+dr, col+dc
                
                if (dr>=0 and dr<rows) and (dc>=0 and dc<cols) and (grid[dr][dc]==0) and ((dr,dc) not in visited):
                    visited.add((dr,dc))
                    q.append((dr,dc))

    lake_count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==0 and (row,col) not in visited:
                BFS(row,col)
                lake_count+=1
    
    print(f"Total lakes: {lake_count}")


arr = [ [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0], 
        [0,1,1,1,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,1,0,1,1,1,0,0,1,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
count_lakes(arr)
arr = [
	[0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
	[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
	[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
	[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
count_lakes(arr)
arr = [
    [1,1,1,1,1],
    [0,1,0,1,1],
    [0,1,0,1,1],
    [0,0,1,0,1],
    [0,0,0,1,1]
]
count_lakes(arr)
arr = [
    [1,1,1,1,1],
    [0,1,0,1,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
]
count_lakes(arr)