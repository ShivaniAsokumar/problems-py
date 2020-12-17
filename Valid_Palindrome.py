""" 
* Remove all spaces
* Remove all non-alphanumeric values

def palindrome(s):
  s = s.replace(" ","")

  re.sub(r'[^A-Za-z0-9]+', '', s)
"""

import re
def isPalindrome(s):
  s = s.lower()
  s = re.sub(r'[^A-Za-z0-9]+', '', s)
  return s[::-1] == s


print(isPalindrome("race a car"))


