'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
'''
from collections import deque

class Solution:
    def fill_boundary(self,grid: list[list[int]])->list[list[int]]:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        visited = set()
        def BFS(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row,col = q.popleft()
                grid[row][col] = 1
                for dr,dc in directions:
                    dr,dc = dr+row, dc+col
                    if (dr>=0 and dr<len(grid)) and (dc>=0 and dc<len(grid[0])) and (grid[dr][dc] ==0) and ((dr,dc) not in visited):
                        q.append((dr,dc))
                        visited.add((dr,dc))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row==0 or row==len(grid)-1 or col ==0 or col ==len(grid[0])-1) and (grid[row][col] ==0) and ((row,col) not in visited):
                    BFS(row,col)
        return grid


    def closedIsland(self, grid: list[list[int]]) -> int:
        remove_boundary_islands = self.fill_boundary(grid)
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        total_islands = 0
        
        def BFS(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row,col = q.popleft()
                grid[row][col] = 1
                for dr,dc in directions:
                    dr,dc = dr+row, dc+col
                    if (dr>=0 and dr<len(grid)) and (dc>=0 and dc<len(grid[0])) and (grid[dr][dc] ==0) and ((dr,dc) not in visited):
                        q.append((dr,dc))
                        visited.add((dr,dc))


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (grid[row][col] ==0) and ((row,col) not in visited):
                    total_islands += 1
                    BFS(row,col)

        return total_islands
    
sol = Solution()

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
print(sol.closedIsland(grid))

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]
print(sol.closedIsland(grid))