""" 
! PROMPT: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array. m and n are the number of elements that are initialized in nums1 and nums2 respectively. 

TODO: Understand
* Input: Two Arrays and two Integers
* Output: Array (num1 in sorted in place)

Base Case:
if n = 0:
    return nums1

* Sorting in-place = Quicksort O(n)

TODO: Pseudocode
for i in range(m + 1, len(nums1)):
    nums1[i] = nums2.pop(0)

call quicksort on nums1
"""

def merge(nums1, m, nums2, n):
    for i in range(m, len(nums1)):
        nums1[i] = nums2.pop(0)
    print(nums1)
    quicksort(nums1, 0, len(nums1) - 1)
    

def quicksort(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quicksort(A, low, pivot - 1)
        quicksort(A, pivot + 1, high)

def partition(A, low, high):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        if (A[j] < pivot):
            i += 1
            A[j], A[i] = A[i], A[j]
    A[high], A[i + 1] = A[i + 1], A[high]
    return i + 1

merge([], 0, [], 0)

