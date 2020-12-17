""" 
!PROMPT: What is the smallest positive number that is evenly divisible by all numbers from 1-20?

TODO: Understand
* Find a number that can be divided evenly by all of the numbers from 1 - 20. 

TODO: Problem Solving
1-3
* Start checking divisibilty at 2
* Start with n + 1
4 / 2 yes
4 / 3 no

5 / 2 no

6 /2 yes
6 /3 yes
// 6 is our answer

// 1 - 3

* Start with n + 1
* Check for divisibility at 2
* If current_number is divisibley by test_number, continue
* Else, stop what you are doing, increment current_number by 1, start again
* return current_number

def highly_divisible():
    current_number = 4
    highly_divisible = True
    for i in range(2, n):
        if current_number isn't divisible by i:
            increment
            highly_divisible = False
            break
    if highly_divisible:
        return current_number
            


"""