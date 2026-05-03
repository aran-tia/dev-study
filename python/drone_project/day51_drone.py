def get_height_commands(commands):
    min_heihgt = 0
    height = 0
    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        if height < min_heihgt:
            min_heihgt = height
    return min_heihgt
commands = ["상승", "하강", "하강", "상승", "하강"]
print(get_height_commands(commands))
