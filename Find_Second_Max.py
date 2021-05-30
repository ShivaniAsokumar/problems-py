""" 
! PROMPT: Find the second largest element in a given list. 

* Input: Array of numbers
* Output: Second largest number

? What happens if an illegal argument is given. => Raise ValueError

* Secong largest number is smaller than max but larger than all other values. 

// Brute Force Solution
* Find the maximum using nested loops. 
* Delete the maximum from the list
* Find the maximum again to get the second largest number.
* Time Complexity: O(n^2)

// Current Solution
* Find the maximum O(n)
* Remove the maximum from array O(n)
* Find the maximum O(n)
* Time complexity = O(3n)

def find_second_maximum(lst):
    maximum = float('-inf')
    for n in lst:
        if n > maximum: 
            maximum = n

    lst.remove(maximum)

    maximum = float('-inf')
    for n in lst:
        if n > maximum: 
            maximum = n

    return maximum

// Testing
arr = [9,2,3,6]
maximum = 9

arr = [2,3,6]
maximum = 6

"""

def find_second_maximum(lst):
    # For invalid inputs
    try:
        maximum = float('-inf')
        for n in lst:
            if n > maximum: 
                maximum = n

        lst.remove(maximum)

        maximum = float('-inf')
        for n in lst:
            if n > maximum: 
                maximum = n
        return maximum
    except ValueError:
        print('Input is invalid. Please enter the correct values')

print(find_second_maximum([4,2,1,5,4]))


# * Better solution with Two Traversals
def find_second_maximum2(lst):
    try: 
        maximum = second_max = float('-inf')
        for n in lst:
            if n > maximum: 
                maximum = n
        
        for n in lst:
            if n > second_max and n != maximum:
                second_max = n

        return second_max
    except ValueError:
        print('Input is invalid. Please enter the correct values')

print(find_second_maximum2([4,2,1,5,4]))

# * One Traversal O(n)
def find_second_maximum3(lst):
    try: 
        maximum = second_max = float('-inf')
        for n in lst:
            if n > maximum: 
                maximum = n
                second_max = maximum

            elif n != maximum and n > second_max:
                second_max = n

        return second_max

    except ValueError:
        print('Input is invalid. Please enter the correct values')

""" 
// Lessons Learned
* There are two ways of solving this problems: one traversal or two traversal. 
* Having just one traversal is less cluttered so even though the time complexity is the same, it is easier to read. 
"""
    