def lowest_point(commands):
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

    return (min_index, min_height)
commands = ["상승", "하강", "하강", "상승", "하강", "상승"]
print(lowest_point(commands))