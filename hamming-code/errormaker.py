import random
from copy import deepcopy
from matrix import Matrix

'''
Takes a list of vectors and an integer as argument. Returns the list of vectors
with 1 random integer (0 or 1) changed to a 0 or 1
'''
def errormaker(encodelist, length):
    errorlist = deepcopy(encodelist)
    for i in range(len(Matrix(errorlist).values)):
        r = random.randint(0, length-1)
        if errorlist[i].values[r][0] == 1:
            errorlist[i].values[r][0] = 0
        else:
            errorlist[i].values[r][0] = 1
    return errorlist


'''
Takes a string of 0's and 1's and an integer (length)
as argument. Returns the string with 1 random digit changed
to a 1 or 0, whatever it wasn't before.
'''
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
