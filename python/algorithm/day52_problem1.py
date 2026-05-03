def get_longest_text(text):

    current_count = 0
    max_count = 0

    for ch in text:
        if ch not in "aeiou":
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
    
    return max_count
text = "aaabbbccddeeiiffgg"
print(get_longest_text(text))