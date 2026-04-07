def count_direction_change(commands):
    prev = 0
    count = 0

    for cmd in commands:
        if cmd == "상승":
            curr = 1
        elif cmd == "하강":
            curr = -1

        if prev == -1 and curr == 1:
            count += 1

        prev = curr
        
    return count

commands = ["상승", "하강", "상승", "상승", "하강", "상승"]
print(count_direction_change(commands))
