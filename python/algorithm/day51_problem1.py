def get_current_numbers(text):
    max_count = 0
    current_count = 0
    for ch in text:
        if ch.isdigit():
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
    return max_count 

text = "ab123cd45ef6789"
print(get_current_numbers(text))
    

    