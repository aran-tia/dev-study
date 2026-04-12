def get_lowest_height(commands):
    min_height = 0
    height = 0
    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1
       

        if height < min_height:
            min_height = height

    return min_height

commands = ["상승", "상승", "하강", "상승", "하강", "하강"]
print(get_lowest_height(commands))