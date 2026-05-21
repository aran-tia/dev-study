def get_pattern(text):
    current_count = 0
    current_start = 0

    max_start = 0
    max_count = 0

    for i in range(len(text)):
        ch = text[i]

        if ch.isupper():
            current_count += 1

            if current_count == 1:
                current_start = i
        else:
            current_count = 0

        if current_count > max_count:
            max_start = current_start
            max_count = current_count

    return (max_count, max_start)
text = "AAABBBCCCCDD"
print(get_pattern(text))
