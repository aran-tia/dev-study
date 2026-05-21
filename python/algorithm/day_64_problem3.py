def get_pattern(text):
    
    current_char = text[0]
    current_count = 1

    result = []

    for i in range(1, len(text)):
        if text[i] == current_char:
            current_count += 1
    
        else:
            result.append((current_char, current_count))
            current_char = text[i]
            current_count = 1
    result.append((current_char, current_count))

    return result
text = "aaabbccccd"
print(get_pattern(text))