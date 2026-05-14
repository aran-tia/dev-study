def compress_commands(commands):
    result = []
    current = commands[0]
    count = 1

    for cmd in commands[1:]:
        if cmd == current:
            count += 1
        else:
            result.append((current, count))
            current = cmd
            count = 1

    result.append((current, count))

    return result


commands = ["상승", "상승", "상승", "전진", "전진", "하강", "하강", "좌회전"]
print(compress_commands(commands))