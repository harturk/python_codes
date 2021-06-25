
"""
Function to rotate strings. The code will always rotate to the left first,
then the left rotated string will be an input parameter to the right rotate function

"""

from itertools import cycle

# Number of times it will rotate to the left
lS = 2
# Number of times it will rotate to the left
rS = 4
# String
s = 'abcdefg'


def leftShifts(string, n):
    # Cycle the string - Ex: string ['a','b','c'] became ['a','b','c','a','b','c'...]
    stringCycled = cycle(string)
    # Convert the string to a list and add it to a variable
    string = list(string)
    # List that will receive the result
    leftShiftedString = []
    for i in range(n):
        # Add n cycle elements to the original string
        # Everytime the function next is called, it will take the next
        string.append(next(stringCycled))
    for i in range(n,len(string)):
        # Take part of the string, where if was added 2 elements, will be removed the first 2 elements
        leftShiftedString.append(string[i])
    return leftShiftedString


def rightShifts(string, n):
    # Right shift works the same, but it seemed to be easier reversing the string
    # and in the end of the function, reverse back
    string = list(reversed(string))
    stringCycled = cycle(string)
    rightShiftedString = []
    for i in range(n):
        string.append(next(stringCycled))
    for i in range(n, len(string)):
        rightShiftedString.append(string[i])
    rightShiftedString = list(reversed(rightShiftedString))
    return rightShiftedString

if __name__ == '__main__':
    print(rightShifts(leftShifts(s,lS),rS))