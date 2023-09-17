# place n queens on an nxn chess board so that no two queens attack each other

# global n
# global board

n = int(input("Enter the value of n:"))
board = []

def get_board():
    for i in range(n):
        nth_list = []
        for j in range(n):
            nth_list.append(0)
        board.append(nth_list)

    # print(board)

def print_board():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("")

# returns true if a queen is safe at a particular square
def is_safe(row, col):
    # checking row and column
    for i in range(n):
        if board[row][i] == 1:
            return False
    for j in range(n):
        if board[j][col] == 1:
            return False
    # checking if there are any attacking pieces in diagonals
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i -= 1
        j -= 1
    
    i = row+1
    j = col+1
    while(i<n and j<n):
        if board[i][j]==1:
            return False
        i += 1
        j += 1

    i = row-1
    j = col+1
    while(i>=0 and j<n):
        if board[i][j]==1:
            return False
        i -= 1
        j += 1
    
    i = row+1
    j = col-1
    while(i<n and j>=0):
        if board[i][j]==1:
            return False
        i += 1
        j -= 1
    return True

def put_queen(total_queens):
    # base condition
    if total_queens == n:
        return True
    
    # rec condition
    for i in range(n):
        for j in range(n):
            # if cell (i,j) is safe, place a queen over there
            if is_safe(i,j):
                board[i][j] = 1
                total_queens += 1
                # if all subsequent  conditions pass, then we return true
                if put_queen(total_queens) == True:
                    return True
                # if we are not able to arrange the subsequent queens in non-attacking squares, then backtrack
                board[i][j] = 0
                total_queens -= 1
    # return False if not able to place the queen in non-attacking square
    return False


# lets run it
get_board()
put_queen(0)
print_board()