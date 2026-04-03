def get_repeat_text(texts):

    

    max_count = 1
    current_count = 1

    for i in range(1, len(texts)):
        if texts[i] == texts[i - 1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > max_count:
            max_count = current_count

    return max_count

text = "aaabbccccd"
print(get_repeat_text(text))