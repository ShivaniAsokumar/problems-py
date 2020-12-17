""" 
!PROMPT: Given a 32-bit signed integer, reverse digits of an integer.

TODO: Understand
* Convert the integer to a string
* Split the string into array
* Reverse the array
* Join the array
* Conver to integer
* Return answer

321 => 123

TODO: Problem Solving

def Reverse_Integer(s):


"""
def Reverse_Integer(num):

  l = list(str(num))
  reversed_list = []
  if l[0] == '-':
    del l[0]
    l.append('-')
  for i in range(len(l)):
    reversed_list.append(l.pop())
  
  result = int(''.join(reversed_list))
  if abs(result) > 2 ** 31 - 1:
    return 0
  return result

print(Reverse_Integer(-1534236469))
