""" 
!PROMPT: You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
    * numberOfBoxesi is the number of boxes of type i.
    * numberOfUnitsPerBoxi is the number of units in each box of the type i.
!You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

! Return the maximum total numer of units that can be put on the truck

TODO: Understand
* Input => boxTypes[numerofBoxes, numberOfUnitsPerBox]
* Output => maximum number of units that can be shipped within the given truck size

// How it works
Example: [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
* Take the boxTypes with the largest unitsPerBox. Multiply them with the numberOfBoxes
* Remove the boxType from the array
* Find the next max unitsPerBox

? Should I use a dictionary

TODO: Match
// Key Operations
* Iterate through array, get the max of arr[i][1].
* Multiply it by arr[i][0]. Keep track of truckSize. 
* Remove the max from the array
* Sum of arr[0] <= truckSize

TODO: Problem Solving
boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Find Max: 3
1 * 3 = 3
truckSize - 1 = 3

boxTypes = [[2,2], [3,1]]
Find Max: 2
if number of boxes < truckSize:
    2 * 2 = 4
    truckSize - 2 = 1

boxTypes = [[3,1]]
Find Max: 1
if number of boxes < truckSize:
else: 
    truckSize * 1 = 1

* Make sure that boxTypes is not an empty array

def maximum_units(boxTypes):
    units = [boxType[1] for boxType in boxTypes]
    sum = 0
    while boxTypes and truckSize > 0:
        maximum = max(units)
        index = units.index(maximum)
        units.pop(index)

        number_of_boxes = boxTypes[index][0]
        units_per_box = boxTypes[index][1]
        if number_of_boxes < truckSize:
           sum += number_of_boxes * units_per_box
           truckSize -= number_of_boxes 
        else:
            sum += truckSize * units_per_box
            truckSize = 0
        boxTypes.pop(index)

    return sum



"""

def maximum_units(boxTypes, truckSize):
    units = [boxType[1] for boxType in boxTypes]
    unit_sum = 0
    while len(boxTypes) > 0 and truckSize > 0:
        maximum = max(units)
        index = units.index(maximum)
        units.pop(index)

        number_of_boxes = boxTypes[index][0]
        units_per_box = boxTypes[index][1]
        if number_of_boxes < truckSize:
           unit_sum += number_of_boxes * units_per_box
           truckSize -= number_of_boxes 
        else:
            unit_sum += truckSize * units_per_box
            truckSize = 0
        boxTypes.pop(index)

    return unit_sum

print(maximum_units([[5,10],[2,5],[4,7],[3,9]], 10))
