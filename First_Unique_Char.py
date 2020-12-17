""" 
!PROMPT: Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

TODO: Understand
* This problem uses Dictionaries
* Count all the letters in the word
* Return the index of the letter that only has count = 1

// Return the FIRST letter that has a count = 1

[l,e,e,t]
dict = {
  l: 1,
  e: 2,
  t: 1
}

values = [1,2,1]
values.index(1) = 0


"""

def First_Unique_Char(s):
  # s = list(s)
  for letter in s:
    if s.count(letter) == 1:
      return s.index(letter)
  return -1

