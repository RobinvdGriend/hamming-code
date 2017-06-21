import random
from copy import deepcopy
from matrix import Matrix
# hier moet ik nog wat opmerkingen aan toevoegen


def errormaker(encodelist, length):
    errorlist = deepcopy(encodelist)
    for i in range(len(Matrix(errorlist).values)):
        r = random.randint(0, length-1)
        if errorlist[i].values[r][0] == 1:
            errorlist[i].values[r][0] = 0
        else:
            errorlist[i].values[r][0] = 1
    return errorlist

def errormakerstring(string, length):
    newstring = ''
    while string != '':
        r = random.randint(0,length-1)
        if string[r] == '1':
            newstring = newstring + string[:r] + '0' + string[r+1:length]
        else:
            newstring = newstring + string[:r] + '1' + string[r+1:length]
        string = string[length:]
    return newstring
