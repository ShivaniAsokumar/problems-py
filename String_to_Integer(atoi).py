import sys
""" 
TODO: Understand
  * Discards whitespaces until the first non-whitespace character is found. 
  * Takes initial + or - sign followed by numbers. 
  * All characters after that number are ingnored
  * If first sequence is not a valid non-whitespace characters, return 0

  ! If the number is out of range, INT_MAX and INT_MIN is returned


- lstrip() string
- convert to int
- if over range, return the numbers

def myAtoi(s):
  s = s.lstrip()
  num = int(s)
  if num > 2**31:
    return max
  else:
    return min

"""

def My_Atoi(str):
  str = str.lstrip()
  if " " in str:
    str = str[:str.index(" ")]
    
  try:
    num = int(float(str))
    if num > 2 ** 31 - 1:
      return 2 ** 31 - 1
    elif num < -2 ** 31: 
      return -2 ** 31
    else:
      return num
  except:
    return 0
  

print(int(float('1.4')))


