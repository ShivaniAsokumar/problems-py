""" 
!PROMPT: A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
    ! - You can pick any two different foods to make a good meal. 

TODO: Understand
* Two-pointer approach
* Complexity: O(n^2) because nested for-loops
* Outer-loop: iterate through every element in array ONCE. Come up with combinations of numbers that add up to be sums of power of 2. 
* Inner-loop: this loop iterates through every element for each outer iteration. 
* Counter keeps track of the different combinations. Counter is returned at the end.

// What makes a sum of a power of 2
1 = 2^0
2 = 2^1
4 = 2^2
8 = 2^3
16 = 2^4
32 = 2^5
64 = 2^6 
...

8/2 = 4/2 = 2/2 = 1 (numer of times we divided = 3. 2^3)
16/2 = 8/2 = 4/2 = 2/2 = 1 (number of times we divided = 4. 2^4)
32/2 = 16/2 = 4/2 = 2/2 = 1 (number of times we divided = 5. 2^5)

* If the sum of two numbers if odd, automatically not a power of 2.
* If the sum of two numbers is even, keep dividing, and if at anypoint, the result is an odd number other than 1, not a power of 2. 
    For example: 10/2 = 5 (odd number and not 1)

// The Comparison

count = 0
for i in range(len(arr) - 1) # Prevents index out of bounds
    for j in range(i+1, len(arr))
        if i + j are power of 2, count++ # Use helper function

return count

? What should be the expected result when the length of array is just 1. But that element is a power of 2. What is that element is not a power of 2. 
"""
import math
def power_of_two(num):
    # if num % 2 != 0 and num != 1:
    #     return False
    
    # while num % 2 == 0:
    #     num /= 2

    # # num is odd
    # if num == 1:
    #     return True
    # else:
    #     return False
    if num == 0:
        return False;
 
    val = (math.log10(num) /
            math.log10(2));

    return math.ceil(val) == math.floor(val)

def countPairs(deliciousness):
    count = 0
    for i in range(len(deliciousness) - 1):
        for j in range(i + 1, len(deliciousness)):
            # print(deliciousness[i], deliciousness[j])
            if power_of_two(deliciousness[i] + deliciousness[j]):
                count += 1

    return count
    

print(countPairs([1,0]))
print(power_of_two(1))