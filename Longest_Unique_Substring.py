""" 
result = ""
length_of_max = 0

i = 0
while i < length of string:
    char = s[i]
    if char is not in result:
        result += char
    if char is in result:
        length_of_max = len(result)
        result = ""
    i += 1

return length_of_max

"""
def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0

    mapping = {}
    start = 0
    max_length = 0

    for i in range(len(s)):
        char = s[i]
        if char in mapping and start <= mapping[char]:
            start = mapping[char] + 1
        else:
            index = i - start + 1
            max_length = max(max_length, index)
        mapping[char] = i
    return max_length

        
print(lengthOfLongestSubstring('pwwwkew'), 3)
print(lengthOfLongestSubstring('bbbbbbb'), 1)
print(lengthOfLongestSubstring('abcabckews'), 7)
print(lengthOfLongestSubstring('a'), 1)
print(lengthOfLongestSubstring('dvdf'), 3)