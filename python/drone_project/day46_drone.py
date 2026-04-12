def get_longest_drone(commands):
    height = 0
    current_count = 0
    max_count = 0

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1
        
        if height != 0:
            current_count += 1
        else:
            current_count = 0
        
        if current_count > max_count:
            max_count = current_count

    return max_count

commands = ["상승", "상승", "하강", "하강", "상승", "상승", "하강"]
print(get_longest_drone(commands))