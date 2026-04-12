def longest_same_height(commands):
    height = 0
    prev_height = 0
    current_count = 1
    max_count = 1

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        if height == prev_height:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count
    
        prev_height = height
    return max_count
commands = ["상승", "상승", "하강", "하강", "상승","하강","상승"]
print(longest_same_height(commands))