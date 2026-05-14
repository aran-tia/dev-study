def get_longest_index(text):
    current_start = 0
    max_start = 0

    current_count = 0
    max_count = 0

    for i in range(len(text)):
        ch = text[i]
        if ch.isdigit():
            current_count += 1

            if current_count == 1:
                current_start = i
        else:
            current_count = 0

        
        if current_count > max_count:
            max_count = current_count
            max_start = current_start
    return (max_start, max_count)

text = "ab123cd45ef6789"
print(get_longest_index(text))