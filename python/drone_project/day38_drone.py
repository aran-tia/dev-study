def get_drone_land(commands):
    height = 0
    count = 0

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        if height == 0:
            count += 1
        
    return count

commands = ["상승", "하강", "상승", "하강", "상승", "하강"]
print(get_drone_land(commands))