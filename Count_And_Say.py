""" 
!PROMPT: Given an integer n, returns the nth term of the count-and-say sequence

TODO: Understand
* Input: nth term that we have to return the count-and-say sequence for (Integer)
* Output: count-and-say sequence (String)
? What is the maximum n value: 30
* Recursive:
    Base Case: count_and_say(1) = "1"
    Recursive Case: count_and_say(n) => count_and_say(n-1)

* There are two parts to this problem: recursive function and converting digits to count-and-say sequence
    // recursive function
    * In the recursive function, we just have to call the count-and-say function for n-1

    // count-and-say
    * Write a function that takes in "3322251"
    * two 3's, three 2's, one 5, one 1
    * RETURN: 23321511
    
    * First split them up by their numbers
    "33 222 5 1" 
    * Split along numbers that are not the same
    ! "33": Length of string = 2, number in string = 3
        // 2 3
    ! "222": Length of string = 3, number in string = 2
        // 3 2
    ! "5": Length of string = 1, number in string = 5
        // 1 5
    ! "1": Length of string = 1, number in string = 1
        // 1 1
    ! Add them all together:
        // 23321511

TODO: Match
* split_digit()
* We need a function that splits the given digit string into a list of individual strings
    // "3322251" => ["33", "222","5","1"]
    * In order to get the digit inside the string, just do string[0]

? How to split the given digits into alike numbers
    
    split_array = []
    curr_str = input_string[0]
    for n in range(1, len(input_string)):
        if (n equals curr_str):
            add it to curr_str
        else:
            append curr_str to split_array
            curr_str = "" # Reset it to empty string so that we can move on to next set of digits
    return split_array

TODO: Pseudocode
def count_and_say(n):
    answer = ""
    if(n == 1): # Base Case
        return "1"
    else:
        split_array = get the split_digit()
        # Iterate through the array
        // For each string in the array, the result is the length + the digit value
        for str in array:
            len = len(str)
            answer = answer + len + str[0] 
    return answer

    // Testing the pseudocode 
    count_and_say(2):
    count_str = ""
    digit_array = split_digit("1") => ["1"]

    for loop:
        count_str = "one 1" => "11"
    
    return value = "11"

""" 
def split_digit(digits):
    split_array = []
    curr_str = digits[0]
    for n in range(1, len(digits)):
        
        if (digits[n] == curr_str[-1]): # If digits[n] is equal to the last char from curr_str
            curr_str += digits[n]
            
        else:
            split_array.append(curr_str)
            curr_str = digits[n] # Reset so we move onto next set of digits
        
    split_array.append(curr_str) # Append curr_str to split_array
    return split_array

def count_and_say(n):
    count_str = ""
    if (n == 1):
        return split_digit(str(n))

    else:   
        # digit_array = split_digit(str(n - 1 )) # Convert n to str because split_digit() only takes string args
        digit_array = split_digit(count_and_say(n - 1))
        # Iterate through the array
        for digit_str in digit_array:
            count_str += str(len(digit_str)) + digit_str[0] # len is integer so we need to cast
            
    return count_str


print(count_and_say(5))





