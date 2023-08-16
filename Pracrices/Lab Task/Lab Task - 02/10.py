def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_4_queens(board, col):
    if col == 4:
        return True
    for i in range(4):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_4_queens(board, col+1) == True:
                return True
            board[i][col] = 0
    return False

board = [[0 for x in range(4)] for y in range(4)]
if solve_4_queens(board, 0) == False:
    print("Solution does not exist")
else:
    for i in range(4):
        for j in range(4):
            print(board[i][j], end = " ")
        print()

