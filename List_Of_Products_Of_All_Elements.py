"""  
!PROMPT: Implement a function that modifies a list so that each index has a product of all the numbers present in the list except the number stored at the index. 

* Input: Array of numbers (int or float)
* Output: Array the product

// Brute Force Approach
* Two loops: one iterates onces, the other iterates for each number in the array
* O(n^2)

// Current Attempt
# 24 = total product
24/1 = 24
24/2 = 12
24/3 = 8
24/4 = 6


result = []
total_product = 1

if 0 in nums:
    del nums[nums.index(0):nums.index(0) + 1]

    for n in nums:
        total_product *= n

    for n in nums:
        if n != 0:
            result.append(total_product/n) # careful with division for floating point

        else:
            result.append(total_product)

else:
    for n in nums:
        total_product *= n
    for n in nums:
        result.append(total_product/n) # careful with division for floating point

return result

* Time Complexity: O(n), which is better than the previous solution

nums = [4,2,1,5,0]
! Special case for zeros
* All indices other than the one that has zero should be zero. 
* The index with the zero should hold the product without the zero

"""

def find_product(nums):
    result = []
    total_product = 1

    if 0 in nums:
        # del nums[nums.index(0):nums.index(0) + 1]

        for n in nums:
            if n != 0:
                total_product *= n

        for n in nums:
            if n != 0:
                result.append(0) # careful with division for floating point

            else:
                result.append(total_product)

    else:
        for n in nums:
            total_product *= n
        for n in nums:
            result.append(total_product/n) # careful with division for floating point

    return result

print(find_product([4,2,1,5,0]))


