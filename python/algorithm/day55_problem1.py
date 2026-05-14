def get_straight(text):
    current_count = 0
    max_count = 0

    current_start = 0
    max_start = 0

    for i in range(len(text)):
        ch = text[i]

        if ch.islower():
            current_count += 1

            if current_count == 1:
                current_start = i
        
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
            max_start = current_start

    return (max_count, max_start)
text = "AAabcDDdefghIIjk"
print(get_straight(text))
        


