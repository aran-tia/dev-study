def get_longest_text(text):
    current_count = 1
    max_count = 0

    for ch in text:
        if ch.isdigit():
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0

    return max_count

text = "a123bb45ccc6789"
print(get_longest_text(text))