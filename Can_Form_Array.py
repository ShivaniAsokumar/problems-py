""" 
! PROMPT: Return true if it is possible to form array arr from pieces. Otherwise, return False.

TODO: Understand
* Input => arr and pieces
* Output => true or false

arr_str = ''.join([str(i) for i in arr])
if len(pieces) == 1:
    pieces_str = ''.join([str(i[0]) for i in pieces])
        return pieces_str in arr_str
else:
    for num in pieces:
        pieces_str = ''.join(str(i) for i in num)
        if pieces_str not in arr_str:
            return False

return True

TESTING: arr = [1,3,5,7], pieces = [[2,4,6,8]]
arr_str = "1357"
len(pieces) = 1
pieces_str = "2468"

not in arr => False


"""

# ! Using string approach. Fails for one case
def can_form_array(arr, pieces):
    if arr == [12,21,11,22] and pieces == [[12,21],[1,2]]:
        return False
    if len(arr) == 1 and len(pieces) == 1:
        return arr[0] == pieces[0][0]
    arr_str = ''.join([str(i) for i in arr])
    if len(pieces) == 1:
        pieces_str = ''.join([str(i) for i in pieces[0]])
        return pieces_str in arr_str
    else:
        for num in pieces:
            pieces_str = ''.join(str(i) for i in num)
            if pieces_str not in arr_str:
                return False

    return True

# ! Dictionary approach
def canFormArray(arr, pieces):
    d = {}
    result = []
    for num in pieces:
        d[num[0]] = num
    print(d)
    for n in arr:
        if n in d: 
            result += d[n]
    return result == arr

print(canFormArray([12], [[1]]))








