def get_most_text(text):
    count = {}

    for ch in text:
        if ch == " ":
            continue
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    max_count = 0
    max_char = ""

    for k, v in count.items():
        if v > max_count or (v == max_count and k < max_char):
            max_count = v
            max_char = k

    return max_char

text = "banana apple"
print(get_most_text(text))