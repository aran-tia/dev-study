def get_count_text(text):
    max_text = 1
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1] and text[i] in "aeiou":
            current_count += 1
        else:
            if text[i] in "aeiou":
                current_count = 1
            else:
                current_count = 0

        if current_count > max_text:
            max_text = current_count

    return max_text

text = "aaeeeiioouu"
print(get_count_text(text))