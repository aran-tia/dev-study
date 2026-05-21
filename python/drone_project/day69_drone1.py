def get_pattern(commands):
    current_cmd = commands[0]
    current_count = 1
    result = []

    for i in range(1, len(commands)):
        if commands[i] == commands[i - 1]:
           current_count += 1
        else:
            result.append((current_cmd, current_count))
            current_cmd = commands[i]
            current_count = 1

    result.append((current_cmd, current_count))
    return result

commands = ["상승", "상승", "상승", "하강", "하강", "정지", "상승"]
print(get_pattern(commands))

