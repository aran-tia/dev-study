def longest_constant(text):
    max_count = current_count = 0

    for n in text:
        if n not in "aeiou":
            current_count += 1
        else:
            current_count = 0

        if current_count > max_count:
            max_count = current_count
    return max_count

text = "abbbccddeeffggg"
print(longest_constant(text))