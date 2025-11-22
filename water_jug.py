""""Water Jug Problem"""
from collections import deque

def water_jug_bfs(x, y, target):
    # To track visited states
    visited = set()
    # Queue for BFS: (jug_x, jug_y)
    queue = deque([(0, 0)])
    
    while queue:
        a, b = queue.popleft()
        
        # If we reached the goal
        if a == target or b == target:
            print(f"Solution found: ({a}, {b})")
            return True
        
        # If this state is already visited
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        
        # Generate all possible next states
        next_states = [
            (x, b),   # Fill jug X
            (a, y),   # Fill jug Y
            (0, b),   # Empty jug X
            (a, 0),   # Empty jug Y
            # Pour from X to Y
            (a - min(a, y - b), b + min(a, y - b)),
            # Pour from Y to X
            (a + min(b, x - a), b - min(b, x - a))
        ]
        
        for state in next_states:
            if state not in visited:
                queue.append(state)
    
    print("No solution possible.")
    return False


# Example usage
if __name__ == "__main__":
    X = 4  # Capacity of Jug X
    Y = 3  # Capacity of Jug Y
    TARGET = 2  # Target amount
    
    water_jug_bfs(X, Y, TARGET)
