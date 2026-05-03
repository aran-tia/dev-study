grid = [
    ["S", ".", "."],
    [".", "X", "."],
    [".", ".", "G"]
]

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
        

print(find_start(grid))
print(find_goal(grid))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

x, y = 1, 1

rows = len(grid)
cols = len(grid[0])

for dx, dy in directions:
    nx = x + dx
    ny = y + dy
    print(nx, ny)

    if 0 <= nx < rows and 0 <= ny < cols:
        if grid [nx][ny] != "X":
            print(nx, ny, "move possible")
        
