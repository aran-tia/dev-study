def get_drone_height(commands):
    height = 0

    for i in range(len(commands)):
        if commands[i] == "up":
            height += 1
        elif commands[i] == "down":
            height -= 1

        if height < 0:
            return i
        
    return -1
commands = ["up", "up", "down", "up", "up","down","down","down","down"]
print(get_drone_height(commands))