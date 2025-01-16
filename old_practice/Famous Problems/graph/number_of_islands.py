'''
Given a 2D grid map if 1's(land) and 0's(water). Count the total number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid as all surrounded by water

Eg. 
11110
11010
11000
00000

Output: 1
'''
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]])->int:
        # if we have empty grid
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        visit = set()
        total_islands = 0

        def runBFS(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c = row+dr, col+dc
                    if ((r in range(rows)) and 
                        (c in range(cols)) and 
                        grid[r][c]=='1' and 
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    runBFS(r,c)
                    # print(f"{r}-{c} - {visit}")
                    total_islands+=1

        return total_islands
    

m = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
m2 = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','1','1']]
s = Solution()
print(s.numIslands(m))
print(s.numIslands(m2))