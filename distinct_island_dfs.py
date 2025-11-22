def numDistinctIslands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    shapes = set()

    def dfs(r, c, base_r, base_c, path):
        # Boundary and visited checks
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 0:
            return
        
        visited[r][c] = True
        # Record relative position of each land cell from base
        path.append((r - base_r, c - base_c))
        
        # Explore in all 4 directions
        dfs(r + 1, c, base_r, base_c, path)
        dfs(r - 1, c, base_r, base_c, path)
        dfs(r, c + 1, base_r, base_c, path)
        dfs(r, c - 1, base_r, base_c, path)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                path = []
                dfs(r, c, r, c, path)
                # Store the shape as a tuple of coordinates
                shapes.add(tuple(path))

    return len(shapes)


# Example Usage
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    print("Number of distinct islands:", numDistinctIslands(grid))
