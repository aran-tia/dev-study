def get_height_drone(commands):
    height = 0

    for i in range(len(commands)):
        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            height -= 1
        
        if height == 0:
            return i
        
    return -1
commands = ["상승", "상승", "하강", "하강", "하강", "상승"]
print(get_height_drone(commands))