"""
The purpose of this code is to open a X csv file and filter the users whom
made login using the card and the users whom doesnt. The difference
between they its on 'Source user', where those whom used card, have
@domain.com.br and those who didn't used don't have it. As so the 'Event Subtype'
will be 'start' for login and 'stop' for logout. We will have
to filter this information as well.
"""

import pandas as pd

# Opening the file and spliting columns by comma
csv = r'C:\Users\User_name\Desktop\csvFile.csv'
# Set a variable with all columns name
col_list = ['IPSIDAlertID','First Time','Source User','Source IP','Destination IP','Event Subtype']
df = pd.read_csv(csv,sep=',',usecols=col_list,header=0)
# Separate both columns with the necessary information into two variables
source_User = df['Source User'].str.split(',',n=1,expand=True)
event = df['Event Subtype'].str.split(',',n=1,expand=True)

dict_Card = dict()
dict_NoCard = dict()
list_Intersection = []
list_Crossed = []

for i, (x,y) in enumerate(zip(source_User.values,event.values)):
    # Zip elements of both columns, Source User and Event Subtype
    # in order to make a sublist with these elements
    list_Crossed.append((x,y))

# Range of all elements
for i in range(len(list_Crossed)):
    # Each row is defined by [i] and [0] is for login ID on that row
    # as well as [i][1] is event subtype of each row
    # We need to remove every useless character from the string
    value = str(list_Crossed[i][0]).strip("[]' ")
    # As people may use upper letters to make login, will be necessary
    # convert everything to lower case, or python won't recognize later
    value = value.lower()
    # We will be able to filter those whom did not use the card
    # by measuring their 'Source User' lenght
    if list_Crossed[i][1] == 'start' and len(value) == 6:
        if value not in dict_NoCard:
            dict_NoCard[value] = 1
        else:
            dict_NoCard[value] += 1
    # As we scan the list of crossed information, will be adding the
    # users whom use the card to login in another dict
    elif list_Crossed[i][0] == 'start' and len(value) == 20:
        if value not in dict_Card:
            dict_Card[value] = 1
        else:
            dict_Card[value] += 1

# Intersect who used both
for i in dict_NoCard.keys():
    if i in dict_Card.keys():
        list_Intersection.append(i)












