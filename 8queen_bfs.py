from collections import deque

def is_safe(queen_positions, row, col):
    """
    Check if placing a queen at (row, col) is safe with respect to existing queens.
    queen_positions: list of column indices where queens are already placed in previous rows
    """
    for r, c in enumerate(queen_positions):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True

def bfs_n_queens(n):
    """
    Solve N-Queens problem using BFS
    Returns a list of solutions, each solution is a list of column indices for each row
    """
    solutions = []
    queue = deque()
    
    # Start with an empty board
    queue.append([])  # Each element represents the positions of queens row by row
    
    while queue:
        current = queue.popleft()
        row = len(current)
        
        if row == n:
            solutions.append(current)
            continue
        
        for col in range(n):
            if is_safe(current, row, col):
                queue.append(current + [col])
    
    return solutions

def print_solutions(solutions):
    for sol in solutions:
        for col in sol:
            print(" ".join("Q" if i == col else "." for i in range(len(sol))))
        print("\n")

# Example usage:
n = 4
solutions = bfs_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions)
