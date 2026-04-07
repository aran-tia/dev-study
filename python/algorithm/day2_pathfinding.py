graph = {
    "Forgotten Crossroads" : [
        {"to": "Greenpath", "require": None},
        {"to": "City of Tears", "require": "dash"}
    ],
    "Greenpath": [
        {"to": "Forgotten Crossroads", "require": None},
        {"to": "Fungal Wastes", "require": None}
    ],
    "Fungal Wastes": [
        {"to": "Greenpath", "require": None}
    ],
    "City of Tears": [
        {"to": "Forgotten Crossroads", "require": "dash"},
        {"to": "Crystal Peak", "require": "wall_jump"}
    ],
    "Crystal Peak": [
        {"to": "City of Tears", "require": "wall_jump"}
    ]
}

def get_next_areas(current, skills):
    result = []
    
    for path in graph[current]:
        to_area = path["to"]
        require = path["require"]

        if require == None or require in skills:
            result.append(to_area)

    return result

from collections import deque

def bfs_area(start, goal, skills):
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
    
        for next_area in get_next_areas(current, skills):
            if next_area not in visited:
                visited.add(next_area)
                q.append(next_area)
                parent[next_area] = current

    return []


print(bfs_area("Forgotten Crossroads", "Fungal Wastes", set()))
print(bfs_area("Forgotten Crossroads", "City of Tear", set()))
print(bfs_area("Forgotten Crossroads", "City of Tears", {"dash"}))