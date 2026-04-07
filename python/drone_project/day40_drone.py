def get_drone_height(commands):
    height = 0 
    max_height = 0
    count = 0

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        if height > max_height:
            max_height = height
            count = 1
        elif height == max_height:
            count += 1


    return count
commands = ["상승", "상승", "하강", "상승", "상승","하강", "상승"]
print(get_drone_height(commands))