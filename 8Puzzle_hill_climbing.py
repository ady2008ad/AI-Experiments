import random

# Heuristic: number of misplaced tiles
def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Generate neighbors by moving the blank tile
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = divmod(index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            # swap blank with target tile
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# Print puzzle
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Hill Climbing algorithm
def hill_climbing(start, goal, max_iterations=1000):
    current = start
    current_h = heuristic(current, goal)
    steps = 0

    print("Initial state:")
    print_board(current)
    print(f"Heuristic: {current_h}\n")

    for _ in range(max_iterations):
        neighbors = get_neighbors(current)
        # Evaluate heuristic for all neighbors
        neighbor_scores = [(n, heuristic(n, goal)) for n in neighbors]

        # Pick the neighbor with the lowest heuristic
        best_neighbor, best_h = min(neighbor_scores, key=lambda x: x[1])

        # If no improvement, stop (local optimum)
        if best_h >= current_h:
            print("Reached local optimum or goal cannot be improved.")
            break

        current, current_h = best_neighbor, best_h
        steps += 1

        print(f"Step {steps}:")
        print_board(current)
        print(f"Heuristic: {current_h}\n")

        if current == goal:
            print("✅ Goal reached!")
            return current

    print("❌ Hill climbing stopped (local optimum reached).")
    return current


# Example usage
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    hill_climbing(start_state, goal_state)
