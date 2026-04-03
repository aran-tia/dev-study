def get_least_text(text):
    count = {}
    for n in text:
        if n in "aeiou":
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            
    min_char = ""
    min_count = float('inf')

    for k, v in count.items():
        if v < min_count or (v == min_count and k < min_char):
            min_count = v
            min_char = k

    return min_char

text = "beautiful"
print(get_least_text(text))