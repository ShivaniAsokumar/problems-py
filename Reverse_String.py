import math

""" 
! PROMPT: Write a function that reverses a string. The input string is given as an array of characters char[].

TODO: Understand
* Reverse an array of characters without reverse()
* Start at the beginning and work toward the middle
* Keep swapping first and last elements


* Have two pointers: one starting from beginning and another one starting from end
// Even Length
  0   1   2   3
['s','h','i','v']


length / 2 = 2  (Half)
* It will stop right before index = 2


// Odd Length
  0   1   2   3   4
['s','h','i','v','a']
[a,v,i,h,s]

length / 2 = 2
* It will stop right before index = 2
* Floor the value so that you don't have floating point numbers

TODO: Problem Solving

def Reverse_String(s):
  half = floor(length/2)
  
  end = length - 1
  for start until half:
    swap start and end
  
  return list

    
"""

# def Reverse_String(s):
#   s.reverse()
#   return s

# Reverse without using the reverse method

def Reverse_String(s):
  middle = math.floor(len(s)/2)
  end = len(s) - 1
  
  for start in range(int(middle)):
    print(s)
    s[start],s[end] = s[end], s[start]
    end -= 1
  
  return s

print(Reverse_String(['s','h','i','v','a']))
  


