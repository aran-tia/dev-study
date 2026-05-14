def get_pattern(text):
    current_count = 0
    current_start = 0

    max_start = 0
    max_count = 0

    for i in range(len(text)):
        ch = text[i]

        if ch.islower():
            if i > 0 and text[i] == text[i - 1]:
                current_count += 1

            else:
                current_count = 1
                current_start = i
        else:
            current_count = 0

        
        if current_count > max_count:
            max_count = current_count
            max_start = current_start

    return (max_count, max_start)

text = "aaabbbbccddeeeeeff"
print(get_pattern(text))