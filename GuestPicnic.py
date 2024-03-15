allGuests = {'Noye' : {'apples' : 5, 'pretzels' : 12},
             'Optio': {'ham' : 5, 'apples' : 10},
             'Runa' : {'cups': 40, 'fishes' : 2}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
    
print('Liczba przyniesionych produktow:')
print (' - Apples           ' + str(totalBrought(allGuests, 'apples')))
print (' - Pretzels         ' + str(totalBrought(allGuests, 'pretzels')))
print (' - ham              ' + str(totalBrought(allGuests, 'ham')))
print (' - cups             ' + str(totalBrought(allGuests, 'cups')))
print (' - Fishes           ' + str(totalBrought(allGuests, 'fishes')))
