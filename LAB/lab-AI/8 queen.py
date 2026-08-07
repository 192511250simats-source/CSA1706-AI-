# 8-Queens Problem using Backtracking

N = 8

# Print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

# Check whether a queen can be placed
def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function
def solve(board, row):

    # All queens are placed
    if row == N:
        return True

    # Try each column
    for col in range(N):

        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
board = [[0 for _ in range(N)] for _ in range(N)]

if solve(board, 0):
    print("Solution for 8-Queens Problem:\n")
    print_board(board)
else:
    print("No solution exists.")
