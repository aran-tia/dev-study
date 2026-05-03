def get_drone(commands):
    height = 0
    max_count = 0

    for i in range(len(commands)):
        if commands == "상승":
            height += 1
        elif commands == "하강":
            height -= 1

        if height < 0:
            return i
    return -1
        
commands = ["상승", "상승", "하강", "상승", "하강","하강"]
print(get_drone(commands))