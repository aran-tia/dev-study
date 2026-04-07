from collections import deque

grid = [
    ["S", ".", ".", "X", "."],
    [".", "X", ".", "X", "."],
    [".", "X", ".", ".", "."],
    [".", ".", "X", "X", "."],
    [".g", ".", ".", ".", "G"]
]

def find_position(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == target:
                return (i, j)
            
def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    q = deque()
    q.append(start)

    visited = set()
    visited.add(start)

    parent = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()

        if (x, y) == goal:
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] != "X" and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))

    if goal not in visited:
        return None
        
    path = []
    cur = goal 

    while cur != start:
        path.append(cur)
        cur = parent[cur]

    path.append(start)
    path.reverse()

    return path
    
def mark_path(grid, path):
    for x, y in path:
        if grid[x][y] != "S" and grid[x][y] != "G":
            grid[x][y] = "*"
    
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

start = find_position(grid, "S")
goal = find_position(grid, "G")

path = bfs(grid, start, goal)

if path is None:
    print("no path found.")
else:
    print("path: ", path)
    mark_path(grid, path)
    print_grid(grid)