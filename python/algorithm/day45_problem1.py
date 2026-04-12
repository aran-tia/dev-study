def get_text(text):
    max_count = 0
    current_count = 0

    for i in range(1, len(text)):
        if text[i].isupper() and text[i] == text[i -1]:
            current_count += 1
        else:
            if text[i].isupper():
                current_count = 1
            else:
                current_count = 0

        if current_count > max_count:
            max_count = current_count

    return max_count

text = "aaBBccDDDDeeFF"
print(get_text(text))

