""" 
!PROMPT: Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

TODO: Understand
* Take each integer and combine them to make a number.
* Add 1 to that number
* Edge case => [9,9,9] Array containing number 9
? Can you return an array of strings containing each digit?

TODO: Problem Solving

123 + 1 = 124
10 + 1 = 11
99 + 1 = 100

def plus_one():
  for n in array:
    convert each n to string
    join string 
    convert string to integer
    add 1
    split into array 
    return array

"""

def plus_one(digits):
  if digits[-1] < 9:
    digits[-1] += 1
    return digits
  else:
    val = int(''.join(map(str,digits))) + 1

    return list(str(val))
    
    
  
  

print(plus_one([9,9,8]))
