"""
Problem: Code a function that count the ways of removing chocolate from a box.
Chocolates can be removed 1 at time or 3 at time. [1,3,1] its different from [3,1,1].


Considerations: I have saw people solving this with recursion method, in a simpler way, but i could not get to
the correct answer. This was the way i have found to find the correct answer. With some know values it worked, but
not sure if will work for every entry.
"""

# Function to calculate the factorial and save the value into a dictionary
def fatorial(fat):
    i = fat
    n = fat
    if i in memo.keys():
        return memo[n]
    else:
        while i > 1:
            i = i - 1
            fat = fat * i
        memo[n] = fat
    return fat
# Entry
box = int(input('Insira a quantidade de chocolates que há na caixa: '))
memo = {}
# Generate an arr of 1 (ones) with size of box.
ways = [1]*box
# Starts the count of ways with 1, because, for a box of 6 elements for example, [1,1,1,1,1,1] is one way.
count = 1
# There is only way of removing if there are less than 3 elements.
if box < 3:
    count = 1
# If equals to 3 or 4, the number of ways is equal to the size of it
elif box == 3 or box == 4:
    count = (len(ways) - 1)
else:
    while True:
# Index 2 must be 1, otherwise will be added more chocolates to the problem
        if len(ways) > 3 and ways[2] == 1:
# Remove 3x 1 (ones) and add 1x 3
            ways.pop(0)
            ways.pop(0)
            ways.pop(0)
            ways.append(3)
            n3 = ways.count(3)
            n1 = ways.count(1)
# Count how many ones and threes are in the arr. If exists one 3 or one 1, the count of this line
# will be equal to the len(arr)
            if n3 <= 1 or n1 <= 1:
                count = count + len(ways)
            else:
# if not, will count combinations of the elements in the arr, excluding repetitions
                count = count + int(fatorial(len(ways))/(fatorial(n3)*fatorial(n1)))
        else:
            break
print(count)
