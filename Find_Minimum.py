def find_minimum(arr):
    minimum = float('inf')
    for n in arr:
        if n < minimum:
            minimum = n
    return minimum

print(find_minimum([100, 12, 34, 40]))
