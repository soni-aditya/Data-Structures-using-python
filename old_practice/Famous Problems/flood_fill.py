'''
Flood Fill Algorithm 🎨
In MS-Paint, when we take the brush 🖌️ to a pixel and click, the color of the region of that pixel is replaced with a new selected color. Following is the problem statement to do this task.
Given a 2D screen, location of a pixel in the screen and a color, replace color of the given pixel and all adjacent same colored pixels with the given color. For example,

screen = [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 1, 1],
                [1, 2, 2, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 2, 2, 0],
                [1, 1, 1, 1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1, 2, 2, 1]]

x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that should replace
the previous color on screen[x][y] and all surrounding pixels with the same color.

Output:

Screen should be changed to following.
screen=[[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 3, 3, 3, 3, 0, 1, 0],
        [1, 1, 1, 3, 3, 0, 1, 0],
        [1, 1, 1, 3, 3, 3, 3, 0],
        [1, 1, 1, 1, 1, 3, 1, 1],
        [1, 1, 1, 1, 1, 3, 3, 1]]
'''
from collections import deque

def flood_fill(grid:list,r:int,c:int,new_color:int):
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    color = grid[r][c]

    q = deque()
    q.append((r,c))
    grid[r][c] = new_color
    while q:
        row,col = q.popleft()
        for dr,dc in directions:
            dr,dc = row+dr, col+dc
            if (dr>=0 and dr<len(grid)) and (dc>=0 and dc<len(grid[0])) and grid[dr][dc]==color:
                q.append((dr,dc))
                grid[dr][dc] = new_color

    print(grid)


screen =       [[1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 1, 1],
                [1, 2, 2, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 0, 1, 0],
                [1, 1, 1, 2, 2, 2, 2, 0],
                [1, 1, 1, 1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1, 2, 2, 1]]
flood_fill(screen,4,4,3)

# [[1, 1, 1, 1, 1, 1, 1, 1], 
#  [1, 1, 1, 1, 1, 1, 0, 0], 
#  [1, 0, 0, 1, 1, 0, 1, 1], 
#  [1, 3, 3, 3, 3, 0, 1, 0], 
#  [1, 1, 1, 3, 3, 0, 1, 0], 
#  [1, 1, 1, 3, 3, 3, 3, 0], 
#  [1, 1, 1, 1, 1, 3, 1, 1], 
#  [1, 1, 1, 1, 1, 3, 3, 1]]