def highest_point(commands):
    height = 0
    max_height = 0
    max_index = -1

    for i in range(len(commands)):
        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            height -= 1

        if height > max_height:
            max_height = height
            max_index = i
        
    
    return (max_height, max_index)

commands = ["상승", "상승", "하강", "하강", "상승", "상승", "상승", "하강", "하강" ]
print(highest_point(commands))
