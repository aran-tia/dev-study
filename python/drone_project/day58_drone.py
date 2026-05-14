def drone_height(commands):
    height = 0
    min_height = 0
    min_index = -1

    for i in range(len(commands)):
        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            height -= 1
        
        if height < min_height:
            min_height = height
            min_index = i

    return (min_height, min_index)

commands = ["상승", "상승", "하강", "하강", "상승", "하강", "하강"]
print(drone_height(commands))