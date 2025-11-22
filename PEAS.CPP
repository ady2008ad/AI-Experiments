# Wumpus World solver using basic reasoning

world = [
    ['S', '', '', 'P'],
    ['', '', '', ''],
    ['', 'W', '', ''],
    ['G', '', '', '']
]

rows, cols = 4, 4
safe = [[False]*cols for _ in range(rows)]  # safe squares
visited = [[False]*cols for _ in range(rows)]

# Directions: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def in_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

def percepts(x, y):
    """Return breeze, stench, glitter"""
    breeze = any(in_bounds(x+dx, y+dy) and world[x+dx][y+dy]=='P' for dx, dy in directions)
    stench = any(in_bounds(x+dx, y+dy) and world[x+dx][y+dy]=='W' for dx, dy in directions)
    glitter = world[x][y]=='G'
    return breeze, stench, glitter

def dfs(x, y):
    """DFS search to find gold safely"""
    if not in_bounds(x, y) or visited[x][y]:
        return False
    visited[x][y] = True
    breeze, stench, glitter = percepts(x, y)
    if world[x][y] in ['P','W']:
        return False
    safe[x][y] = True
    if glitter:
        print(f"Gold found at ({x},{y})")
        return True
    # Explore neighbors
    for dx, dy in directions:
        if dfs(x+dx, y+dy):
            return True
    return False

# Start from S at (0,0)
dfs(0,0)

print("\nSafe Cells:")
for row in safe:
    print(row)
