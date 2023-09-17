# find total ways in which n queens can be places on an nxn chess board 
# so that no two queens attack each other

# place n queens on an nxn chess board so that no two queens attack each other


total_ways = 0
# Function to check if two queens threaten each other or not
def isSafe(board, row, col):
 
    # return false if two queens share the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
 
    # return false if two queens share the same `\` diagonal
    (i, j) = (row, col)
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (row, col)
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
def printSolution(board):
    global total_ways
    for r in board:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
    total_ways+=1
 
 
def nQueen(board, row):
 
    # if `N` queens are placed successfully, print the solution
    if row == len(board):
        printSolution(board)
        return
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(board)):
 
        # if no two queens threaten each other
        if isSafe(board, row, i):
            # place queen on the current square
            board[row][i] = 1
 
            # recur for the next row
            nQueen(board, row + 1)
 
            # backtrack and remove the queen from the current square
            board[row][i] = '0'
 
 
if __name__ == '__main__':
 
    # `N × N` chessboard
    N = 4
 
    # `board[][]` keeps track of the position of queens in
    # the current configuration
    board = [['0' for x in range(N)] for y in range(N)]
 
    nQueen(board, 0)
    print(f"Total ways: {total_ways}")