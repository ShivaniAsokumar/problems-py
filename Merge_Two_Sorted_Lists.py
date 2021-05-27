""" 
!PROMPT: Merge two sorted lists into another sorted list

* Input: Two sorted arrays
* Output: One sorted array merged

? What is the most important value of the problem: Time or Space

? What if the user were to implement a string array

? What if one of the elements is None

? Can we assume that the inputs are only going to be integer arrays

? Are there duplicates in the array 
// Brute Force
- Combine the two lists and add to a new list
- use the python .sorted() method
- Time Complexity is O(n*logn)
- Space Complexity  O(1)
* We can do better if we trade off some Space. Depends on what is more important. 

// My Solution
def merge_lists(lst1, lst2):
    result = []
    idx_1 = 0
    idx_2 = 0
    
    while (idx_1 < len(lst1) and (idx_2 < len(lst2))):
        if element in lst1 < element in lst2:
            add element in lst1 to result array
            idx_1++
            
        else:
            add element in lst2 to result
            idx_2++
             
    # If one of the array still hasn't been fully traversed, add all the elements to result
    while (idx_1 < len(lst)):
        add element to result
        idx_1++
        
    while (idx_2...):
        add element to result
        idx_2++
       
    return result
* Time Complexity: O(n + m)

// Testing
merge_list([1,3,4,5], [2,6,7,8])
merge_list([4,5,6], [-2,-1,0,7])
"""
import numpy as np
def merge_arrays(lst1,lst2):
    idx_1 = 0
    idx_2 = 0
    result = []

    # What if a user inputs a string array?
    # What if one of the elements is None?
    try:
        # Go through both the arrays and add elements that are smaller first
        while (idx_1 < len(lst1) and idx_2 < len(lst2)):
            if (lst1[idx_1] < lst2[idx_2]):
                result.append(lst1[idx_1])
                idx_1 += 1
            else:
                result.append(lst2[idx_2])
                idx_2 += 1
        
        # If one of the arrays still hasn't been fully traversed, add the rest to result
        while (idx_1 < len(lst1)):
            result.append(lst1[idx_1])
            idx_1 += 1
        
        while (idx_2 < len(lst2)):
            result.append(lst2[idx_2])
            idx_2 += 1
        
        return result
    except TypeError:
        print("Array elements must be integers. Please fix your input. ")

large_array = np.arange(100000000000)
print(merge_arrays(large_array, [-2,0,0,7]))