from collections import deque

grid = [
    ["S", ".", "."],
    [".", "X", "C"],
    [".", ".", "G"]
]
battery = 4

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i, j)
    

def find_goal(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "G":
                return (i, j)

start = find_start(grid)
goal = find_goal(grid)


directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

rows = len(grid)
cols = len(grid[0])

q = deque()
q.append(start)

visited = set()
visited.add(start)

parent = {}

while q:
    x, y = q.popleft()

    if (x, y) == goal:
        print("arrive!", (x, y))
        break

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] != "X" and (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))

path = []
current = goal

while current != start:
    path.append(current)
    current = parent[current]

path.append(start)
path.reverse()

print("path:")
print(path)

used_battery = len(path) - 1
if battery <= battery:
    print("used battery: ", used_battery)
    print("Destination reachable")
    print("over battery: ", battery - used_battery)

    
    for x, y in path:
        if grid[x][y] != "S" and grid[x][y] != "G":
            grid[x][y] = "*"

else:
    print("Low battery")
    print("Destination not reachable")
    print("an insufficient battery: ", used_battery - battery)


print("course:")
for row in grid:
    print(" ".join(row))




