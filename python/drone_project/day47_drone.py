def get_height_drone(commands):
    height = 0
    current_count = 0
    max_count = 0

    current_start = 0
    max_start = 0

    for i in range(len(commands)):

        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            height -= 1

        if height > 0:
            current_count += 1

            if current_count == 1:
                current_count = i
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
            max_start = current_start

    return (max_start, max_count)

commands = ["상승", "상승", "하강", "상승", "상승", "하강", "하강", "상승"]
print(get_height_drone(commands))
