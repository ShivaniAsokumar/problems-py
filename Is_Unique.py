""" 
! PROMPT: Determine if a string has all unique characters without using any additional data structures.
""" 

def is_unique(string):
    string = string.lower()

    for i in range(len(string) - 1):
        char = string[i]
        for j in range(i + 1, len(string)):
            compare_char = string[j];
            if char == compare_char:
                return False

    return True

print(is_unique('Hel'))