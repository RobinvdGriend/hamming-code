'''
Het doel van deze comment is obscuur
en qua geheugengebruik is het duur
je vraagt je vast af, maar waarom?
Het antwoord is, heel saai, daarom
'''


class Matrix:

    def __init__(self, values):
        self.values = values

    '''returns transpose'''

    def transpose(self):
        new_matrix = []
        for i in range(len(self.values[0])):
            new_row = []
            for j, row in enumerate(self.values):
                new_row.append(self.values[j][i])
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    '''
    takes two matrices A and B as arguments and returns AB. Overrides the @
    operator
    '''

    def __matmul__(self, other):
        new_matrix = []
        for i, row in enumerate(self.values):
            new_row = []
            for k in range(len(other.values[0])):
                counter = 0
                for j, element in enumerate(row):
                    counter += element * other.values[j][k]
                new_row.append(counter)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    ''' adds two matrices '''

    def __add__(self, other):
        new_matrix = []
        for i, row in enumerate(self.values):
            new_row = []
            for j, element in enumerate(row):
                new_element = element + other.values[i][j]
                new_row.append(new_element)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    ''' takes modulo two of each entry in the matrix'''

    def getbinary(self):
        new_matrix = []
        for row in self.values:
            new_row = []
            for element in row:
                new_element = element % 2
                new_row.append(new_element)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
