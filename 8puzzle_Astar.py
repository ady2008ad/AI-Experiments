import heapq

# Manhattan Distance Heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):  # skip 0 (blank)
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# Generate valid neighbors by moving the blank tile
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
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors


# Print puzzle neatly
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# A* Search Algorithm
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), 0, start, []))
    visited = set()

    while open_set:
        f, g, state, path = heapq.heappop(open_set)

        if state == goal:
            print("✅ Goal reached!")
            print(f"Moves required: {g}\n")
            for step in path + [state]:
                print_board(step)
            return

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [state]))

    print("❌ No solution found.")


# Example usage
if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    a_star(start_state, goal_state)
