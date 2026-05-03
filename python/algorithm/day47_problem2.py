def get_longest_text(text):
    current_count = 1
    max_count = 1
    max_char = [0]
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_char = text[i]


    return (max_count, max_char)

text = "aaabbccccddeee"
print(get_longest_text(text))