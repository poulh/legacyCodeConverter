def isSafe(board, row, col, N):
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solveNQueens(board, row, N):
    if row == N:
        # Print the solution
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        print()
        return

    for col in range(N):
        if isSafe(board, row, col, N):
            board[row][col] = 'Q'
            solveNQueens(board, row + 1, N)
            board[row][col] = '*'  # Backtrack

def printNQueens(N):
    board = [['*' for _ in range(N)] for _ in range(N)]
    solveNQueens(board, 0, N)

N = int(input("Enter the size of the chessboard (N): "))
printNQueens(N)
