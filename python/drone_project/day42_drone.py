def get_drone_height(commands):
    height = 0

    for i in range(len(commands)):
        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            height -= 1

        if height == -2:
            return i
        
    return -1

commands = ["상승", "하강", "하강", "하강"]
print(get_drone_height(commands))