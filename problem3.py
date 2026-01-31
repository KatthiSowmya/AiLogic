def longest_valid_segment(s):
    char_index = {}
    max_length = 0
    start = 0
    for end in range(len(s)):
        char = s[end]
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    return max_length
s = input().strip()
print(longest_valid_segment(s))