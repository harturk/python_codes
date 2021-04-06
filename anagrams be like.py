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

s = input('Insira uma string: ')

per = int(permutate_num(s)/permutate_denom(s))
print(f'O número de anagramas possíveis para a string {s} é: {per}')
