grid = [
    ["S", ".", ".", "X", "."],
    [".", "X", ".", "X", "."],
    [".", "X", ".", ".", "."],
    [".", ".", "X", "X", "."],
    [".", ".", ".", ".", "G"]
]

def find_position(grid, target):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
           if grid[i][j] == target:
               return (i, j)
           
def move_directions(start):
    row = start[0]
    col = start[1]
    
    result = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for move in moves:
        new_row = row + move[0] 
        new_col = col + move[1]

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] != "X":
                result.append((new_row, new_col))
        
    return result


from collections import deque

def bfs(start, goal):
    q = deque()
    q.append(start)

    visited = set()
    visited.add(start)
    parent = {}

    while q:
        current = q.popleft()
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()
            return path
        for next_pos in move_directions(current):
            if next_pos not in visited:
                visited.add(next_pos)
                q.append(next_pos)
                parent[next_pos] = current

    return []     


start = find_position(grid, "S")
goal = find_position(grid, "G")
path = bfs(start, goal)

for row, col in path:
    if grid[row][col] != "S" and grid[row][col] != "G":
        grid[row][col] = "*"



print("start: ", start)
print("arrive: ", goal)
print("path:", path)

for line in grid:
    print(*line)