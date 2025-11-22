from collections import deque

# Function to display a puzzle board
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Function to generate all valid next states
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # find the blank position
    # Possible moves (Up, Down, Left, Right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, col = divmod(index, 3)

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap blank (0) with the adjacent tile
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# BFS to solve the 8-puzzle
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        # Goal test
        if state == goal:
            print("✅ Solution found!")
            print(f"Moves required: {len(path)}")
            print("Path:")
            for step in path:
                print_board(step)
            return

        # Explore all possible moves
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    print("❌ No solution found.")

# Example usage
if __name__ == "__main__":
    # Initial and goal configurations
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    bfs(start_state, goal_state)
