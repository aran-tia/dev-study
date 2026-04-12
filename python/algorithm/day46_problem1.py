def get_longest_text(text):
    current_count = 0
    max_count = 0

    for ch in text:
        if ch.islower():
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return current_count

text = "AAaaBBbbbccDDDdeee"
print(get_longest_text(text))