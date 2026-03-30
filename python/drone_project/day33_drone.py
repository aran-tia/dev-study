def lowest_height(commands):
    height = 0
    min_height = 0

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1
        else:
            continue
    
        if height < min_height:
            min_height = height

    return min_height

commands= ["상승", "상승", "하강", "상승", "정지", "하강", "하강"]