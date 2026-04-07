def get_long_text(text):
    max_count = 0
    current_count = 0

    for n in text:
        if n in "aeiou":
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count

    return max_count

text = "aaeeeiioouu"
print(get_long_text(text))