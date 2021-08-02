"""
This thing is so big for just calculate anagrams number. Well, I followed the same logic till the end and
not proud of that. I have found easier approaches but didnt test it.
What I follow: Anagrams it is a sort of combination with/without repetition. It work by following
(number_available_spaces)!/(repeted_letter1! * repeted_letter2! * repeted_letterN!)
So I had split it up in 2 fuctions, one to calculate the numerater and  the other, the denominator. In this second one I could use Map
but I just learned about later. I've also code a function to take the string, split it into a list, and return this list and
its size. This one was totally unnecessary, but I enjoy string manipulation.
"""

def convert_string(s):
    strList = []
    strList[:0] = s
    lenList = len(strList)
    return strList, lenList

def permutate_num(s):
    fact_len = 1
    lenList = convert_string(s)[1]
    while lenList > 0:
        fact_len = lenList * fact_len
        lenList = lenList - 1
    return fact_len

def permutate_denom(s):
    strList = convert_string(s)[0]
    strSet_sr = set(strList)
    strList_sr = list(strSet_sr)
    strList_r = [item for item in strList if item not in strList_sr or strList_sr.remove(item)]
    per = []
    myset = set(strList_r)
    mylist = list(myset)
    for i in range(len(mylist)):
        cont = 0
        for j in range(len(strList)):
            if mylist[i] == strList[j]:
                cont = cont + 1
        per.append(cont)
    factList = []
    for item in per:
        fact = 1
        for number in range(1, item+1):
            fact = fact * number
        factList.append(fact)
    product = 1
    for item in factList:
        product = product * item
    return product

# Insert a string to 'anagrate'
s = input('Insert a string: ')

# Calculate and return the result
per = int(permutate_num(s)/permutate_denom(s))
print(f'The number of anagrams to the string {s} is: {per}')
