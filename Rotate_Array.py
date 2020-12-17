""" 
!PROMPT: Given an array, rotate the array to the right by k steps, where k is non-negative.

TODO: Understand
* Input => nums {integer Array}, k{integer value}
* Output => array

* [1,2,3,4], k = 2
  [4,1,2,3]
  [3,4,1,2]
* Keep adding the last element in the array until you reach k-value.

//Edge Cases:
? What is k is greater than the len of list
  * It should keep roting array until k

TODO: Problem Solving
i = 0
while i is less than k:
  pop()
  insert(0,popped item)
return the list

rotate_array([1,2,3,4], k = 2)
list = [4,1,2,3]
i = 1
  list.pop() => list = [4,1,2]
  insert(0,list.pop())
  list = [3,4,1,2]
  i++
  
"""

# def Rotate_Array(nums, k):
#   i = 0
#   while i < k:
#     nums.insert(0,nums.pop())
#     i += 1
#   return nums

def Rotate_Array(nums, k):
  i = 0
  while i < k:
      nums.insert(0,nums.pop())
      i += 1
  return nums

print(Rotate_Array([1,2,3,4,5,6,7], 3))





""" 
TODO: Review
* Time Complexity: O(n)
"""