import numpy as np

# entry value with know answer
s = np.array([[5,3,4],[1,5,8],[6,4,2]])

def ways_to_magicSquare():
    # Creating an array with all magic squares possibilities
    magic = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    possible_magic_squares = []
    possible_magic_squares.append(magic)
    possible_magic_squares.append(np.flipud(magic))
    possible_magic_squares.append(np.rot90(magic,1))    # Rotate 90°
    possible_magic_squares.append(np.flipud(np.rot90(magic,1)))
    possible_magic_squares.append(np.rot90(magic,2))    # Rotate 180°
    possible_magic_squares.append(np.flipud(np.rot90(magic, 2)))
    possible_magic_squares.append(np.rot90(magic,3))    # Rotate 270°
    possible_magic_squares.append(np.flipud(np.rot90(magic, 3)))
    # Mirror all matrix
    return possible_magic_squares

def min_cost(s):
    min_cost = float('inf')
    possible_magic_squares = ways_to_magicSquare()
    # Iterates over all elements to find which combination has the lowest cost
    for matrix in possible_magic_squares:
        cur_cost = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cur_cost = cur_cost + np.abs(s[i][j]-matrix[i][j])
        if cur_cost < min_cost:
            min_cost = cur_cost
    return min_cost

print(min_cost(s))
