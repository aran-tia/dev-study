def get_text(text):
    max_count = 0
    current_count = 0


    for ch in text:
        if ch in "aeiou":
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
        
    return max_count

text = "aaabbceeeiioouuubbb"
print(get_text(text))