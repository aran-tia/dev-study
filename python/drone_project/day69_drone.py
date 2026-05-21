def get_height(commands):
    height = 0
    result = []

    for i in range(len(commands)):
        if commands[i] == "상승":
            height += 1
        elif commands[i] == "하강":
            heihgt -= 1

        result.append(height)
commands = ["상승", "상승", "하강", "상승"]
print(get_height(commands))