# reverse a string
def reverse_string(s):
    return s[::-1]

# check anagram
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# first non-repeating character
def first_non_repeating_char(s):
    for ch in s:
        print(s.count(ch))
        if s.count(ch) == 1:
            return ch
    return None

    