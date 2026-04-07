def get_longest_text(text):

    max_count = 1
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1] and text[i] not in "aeiou":
            current_count += 1
        else:
            current_count = 0
        
        if current_count > max_count:
            max_count = current_count
    return max_count

text = "aaabbbbccddee"
print(get_longest_text(text))