def get_drone(commands):
    height = 0

    result = []

    for cmd in commands:
        if cmd == "상승":
            height += 1
        elif cmd == "하강":
            height -= 1

        result.append(height)
    return result
commands= ["상승", "상승", "하강", "상승"]
print(get_drone(commands))