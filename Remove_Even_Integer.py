""" 
!PROMPT: Remove all even integers from a given list. 

TODO: Notes
* Input: random integers (list)
* Output: odd integers (list)

? What is the most important goal of the problem: Time or Space

// Brute Force Solution
* Iterate through every single number and manually check if the number is even or odd. 

def remove_even(lst):
    for i in lst: 
        if i % 2 == 0: 
            lst.remove(i) 
    return lst

    * Time Complexity: O(n^2), which is not the best case to work with

// My Solution
def remove_even(lst):
    odd = [] // O(1)
    for i in lst: // O(n)
        if i % 2 != 0: // O(n)
            odd.append(i) // O(n)
        
    return odd // O(1)

    * Time complexity: O(n)

// My Solution - 2
def remove_even(lst):
    odd = [i for i in lst if i % 2 != 0]

    return odd

    * Time Complexity: O(n) but the code is cleaner and more "pythonic"
"""

def remove_even(lst):
    odd = [i for i in lst if i % 2 != 0]

    return odd



