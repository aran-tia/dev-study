grid = [
    ["S", ".", "."],
    [".", "X", "."],
    [".", ".", "G"]
]

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i, j)
            
def find_goal(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid [i][j] == "G":
                return (i, j)

print_grid(grid)

start = find_start(grid)
goal = find_goal(grid)


print(start)
print(goal)


from collections import deque

q = deque()
q.append(start)

visited = set()
visited.add(start)

x, y = q.popleft()
print(x, y)
print(visited)

rows = len(grid)
cols = len(grid[0])


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    print(nx, ny)

if 0 <= nx < rows and 0 <= ny < cols:
    print("가능: ", nx, ny)