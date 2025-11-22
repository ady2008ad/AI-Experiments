# 8 Queens Problem using Backtracking

N = 8  # board size

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Check if placing a queen at board[row][col] is safe
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve N-Queens
def solve_nqueens(board, row):
    if row == N:
        print("Solution found:")
        print_board(board)
        return True  # print one solution; use return False to find all

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # place queen
            if solve_nqueens(board, row + 1):
                return True  # stop at first solution
            board[row][col] = 0  # backtrack

    return False

# Driver code
if __name__ == "__main__":
    chessboard = [[0] * N for _ in range(N)]
    if not solve_nqueens(chessboard, 0):
        print("No solution exists.")
