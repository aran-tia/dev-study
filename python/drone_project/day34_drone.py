def count_revisit(commands):
    height = 0
    visited = [0]
    count = 0

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        if height in visited:
            count += 1
        else:
            visited.append(height)

        
    return count

commands = ["상승", "상승", "하강", "상승", "하강", "하강", "상승"]
print(count_revisit(commands))