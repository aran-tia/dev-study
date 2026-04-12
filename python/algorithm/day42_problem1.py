def get_longest_text(text):
    current_count = 1
    max_count  = 1
    max_char = text[0]

    for i in range(1, len(text)):
        if text[i] == " ":
            current_count = 0
            continue

        if text[i] != " " and text[i] == text[i -1]:
           current_count += 1
        else:
           current_count = 1

        if current_count > max_count:
           max_count = current_count
           max_char = text[i]

    return max_char
text = "aa bb ccc dddd"
print(get_longest_text(text))