import random
from copy import deepcopy
from matrix import Matrix
# hier moet ik nog wat opmerkingen aan toevoegen


def errormaker(encodelist):
    errorlist = deepcopy(encodelist)
    for i in range(len(Matrix(errorlist).values)):
        r = random.randint(0, 6)
        if errorlist[i].values[r][0] == 1:
            errorlist[i].values[r][0] = 0
        else:
            errorlist[i].values[r][0] = 1
    return errorlist
