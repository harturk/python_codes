# Check the balance ([{
"""
Code a function that check if a string of ([{ its balance.
Balance means for every open there is a closed one.
"""

string = input('Insert a string: ')
# Transforms that string to a list
lista = list(string)
# List of opened
inicio = ('(', '[', '{')
# List of closed
fim = (')', ']', '}')
# Variable to save an index
ind = 0
# Variable to memorize a value
memo = 0
# List that will be used to check its balance
lista2 = []
# Sort the list to faster results and to start if opened ones
lista = sorted(lista)
j = 1
while j != 0:
    for i in range(len(lista)):
        if lista[i] in inicio:
# Save the index of the first scanned element, looking on the 'inicio' list
            ind = inicio.index(lista[i])
# Checks if the fim[index of 'inicio'] is on the list, if not break the loop and return unbalance
            if fim[ind] in lista:
# If it is, will save a pair to the lista2
                memo = lista[i]
                lista2.append(memo)
                memo = fim[ind]
                lista2.append(memo)
            else:
                print('unbalance')
                j = 0
                break
# As for each element scanned in the first loop, was save a pair in lista2, the lenght of both lists
# must be equal in order to be balance
    if len(lista) == len(lista2):
        print('balance')
        j = 0
    else:
        print('unbalance')
        j = 0
