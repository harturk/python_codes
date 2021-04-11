"""
Code a function that, from a start point on the first row, calculates the maximum value path.
The path must go down or diagonal.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# p is the starter point
p = 1
maxSum = m
pickSum = []
sum = None
for i in range(len(m)-1, 0, -1):
    m[i] = maxSum[i]
    for j in range(len(m)):
        # Clear the multiplications list everytime that goes to a new column
        pickSum.clear()
        # Condition to enter in the left column (first)
        if (i - 1) >= 0 and (j - 1) < 0:
            # Sum the current position with the above neighbor
            sum = m[i-1][j] + m[i][j]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Sum the current position with the diagonal right
            sum = m[i-1][j] + m[i][j+1]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Saves the maximum value for this position
            maxSum[i-1][j] = max(pickSum)
            # Condition to enter in the middle column (middle ones if 4x4)
        elif (i - 1) >= 0 and (j - 1) >= 0 and (j + 1) <= (len(m[0]) - 1):
            # Sum the current position with the diagonal left
            sum = m[i-1][j] + m[i][j-1]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Sum the current position with the above neighbor
            sum = m[i-1][j] + m[i][j]
            pickSum.append(sum)
            # Sum the current position with the diagonal right
            sum = m[i-1][j] + m[i][j+1]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Saves the maximum value for this position
            maxSum[i-1][j] = max(pickSum)
            # Condition to enter in the right column (last)
        elif (i - 1) >= 0 and (j + 1) >= (len(m[0])-1):
            # Sum the current position with the diagonal left
            sum = m[i-1][j] + m[i][j-1]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Sum the current position with the above neighbor
            sum = m[i-1][j] + m[i][j]
            # Put the calculate value into a list
            pickSum.append(sum)
            # Saves the maximum value for this position
            maxSum[i-1][j] = max(pickSum)

print(maxSum[0][p])