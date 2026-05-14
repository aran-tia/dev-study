def get_longest(text):
    current_count = 0
    current_start = 0
    max_count = 0
    max_start = 0

    for n in range(len(text)):
        ch = text[n]

        if ch.isupper():
            if n > 0 and text[n] == text[n-1]
            current_count += 1

            if current_count == 1:
                current_start = n

        else:
            current_count = 0
        
        if current_count > max_count:
            max_count = current_count
            max_start = current_start

    return (max_count, max_start)
text = "aaBBCCCDDDDeFF"
print(get_longest(text))


