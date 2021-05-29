""" 
!PROMPT: Given an array, return the first recurring character. If there are no recurring characters, return None

? Is the array limited to integers or are strings are allowed as well.
? What happens if the harray is empty. => return None

* There can be multiple recurring characters, but need to return the FIRST character. 
* Use dictionaries to keep track of the characters. 

// Brute Force Solution
* Nested loops. First loop iterates once. Each time check if that character is equal to the other characters in the array. If yes, return that character immediately. 
* Not great because O(n^2)

// Current Solution
* Use dictionaries to keep track of characters. 
def first_recurring_char(arr):
    tracker = {}
    if (arr):
        for char in arr:
            if tracker[char]: // Only takes O(1) for dictionaries
                return char
            else:
                tracker[char] = True 
        return None
    else:
        return None

* More efficient because Time Complexity = O(n)

// Testing
arr = ['s','a','b','c','s','a','b','c']


tracker = {
's': True,
'a': True,
'b': True,
'c': True
}

return 's'


"""

def first_recurring_char(arr):
    tracker = {}
    if (arr):
        for char in arr:
            if char in tracker: # Only takes O(1) for dictionaries
                return char
            else:
                tracker[char] = True 
        return None
    else:
        return None

print(first_recurring_char(['s','a','b','c','s','a','b','c']))
print(first_recurring_char([2,5,1,2,3,5,1,2,4]))
print(first_recurring_char([2,1,1,2,3,5,1,2,4]))
print(first_recurring_char(['s',2,'s',2,1,1,5]))