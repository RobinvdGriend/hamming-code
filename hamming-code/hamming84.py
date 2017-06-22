from matrix import Matrix
from math import log

# Generator matrix
generator_matrix = Matrix([
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 0]
]).transpose()
length = len(generator_matrix.values)

parity_check_matrix = Matrix([
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1]
])
parity_check_matrixtrans = parity_check_matrix.transpose()


''' makes a dictionary for the paritycheck matrix '''
dictionary = {'place': 'value'}
for i in range(len(parity_check_matrixtrans.values)):
    value = 0
    for k in range(len(parity_check_matrixtrans.values[i])):
        value = value + parity_check_matrixtrans.values[i][k] * 2 ** k
        dictionary[i] = value
dictionary = {value: place for place, value in dictionary.items()}

'''
Takes binary vector of length 4 and adds the parity bits
Returns result as vector
'''


def encodemessage(message):
    vector_with_paritybits = generator_matrix@(message.transpose())
    return vector_with_paritybits.getbinary()


''' Takes a 7 x 1 matrix '''


def repairmessage(message):
    vector = (parity_check_matrix@message).getbinary()
    checker = True
    # checks if the return vector is the zero vector. If this is the case
    # checker = True, and there is no mistake
    for i in range(len(vector.values)):
        if vector.values[i][0] == 1:
            checker = False
    if not checker:
        # finds out at what position the mistake is and saves it as
        # counter
        counter = 0
        for i in range(len((vector.values))):
            counter += vector.values[i][0] * 2 ** i
    else:
        # in this case checker = True, so it returns the message
        return message
    new_message = message.values
    # fixes the message
    wrongbit = dictionary[counter]
    if new_message[wrongbit][0] == 1:
        new_message[wrongbit][0] = 0
    else:
        new_message[wrongbit][0] = 1
    return Matrix(new_message)


''' adds paritybits to entire message '''


def encodeentiremessage(message):
    new_list = []
    for matrix in message:
        new_list.append(encodemessage(matrix))
    return new_list


'''
repairs entire message
'''


def repairentiremessage(message):
    new_list = []
    for matrix in message:
        new_list.append(repairmessage(matrix))
    return new_list


'''
takes a 7x1 vector, destroys the parity bits and returns
what is left
'''


def destroyparitybits(message):
    new_message = message.values
    paritybits = [(2**x) - 1 for x in range(int(log(length, 2) + 1))]
    new_message = [i for j, i in enumerate(new_message) if j not in paritybits]
    return Matrix(new_message)


''' destroys the parity bits from the message and returns the result '''


def destroyallparitybits(message):
    new_list = []
    for matrix in message:
        new_list.append(destroyparitybits(matrix))
    return new_list
