class matrix:

  def __init__(self, values):
    self.values = values
  
  #takes two arguments row and column and return the element in row
  #row and column column
  def element(self, row, column):
    return self.values[row - 1][column - 1]
  
  #takes two matrices A and B as arguments and returns AB. Overrides the * operator
  def __mul__(self, other):
    new_matrix = []
    for i, row in enumerate(self.values):
      new_row = []
      for k in range(len(other.values[0])):
        counter = 0
        for j, element in enumerate(row):
          counter += element*other.values[j][k]
        new_row.append(counter)
      new_matrix.append(new_row)  
    return matrix(new_matrix)

  #adds two matrices
  def __add__(self, other):
    new_matrix = []
    for i, row in enumerate(self.values):
      new_row = []
      for j, element in enumerate(row):
        new_element = element + other.values[i][j]
        new_row.append(new_element)
      new_matrix.append(new_row)
    return new_matrix

  
  #takes modulo two of each entry in the matrix    
  def getbinary(self):
    new_matrix = []
    for row in self.values:
      new_row = []
      for element in row:
        new_element = element%2
        new_row.append(new_element)
      new_matrix.append(new_row)
    return new_matrix
  
  def __str__(self):
    return str(self.values)

#the encodematrix
G = matrix([
  [1, 1, 0, 1],
  [1, 0, 1, 1],
  [1, 0, 0, 0],
  [0, 1, 1, 1],
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 1]
  ])

#the parity check matrix
H = matrix([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 1, 0, 0, 1, 1],
  [0, 0, 0, 1, 1, 1, 1]
  ])

#takes a string with a four 0's or 1's as argument and adds the parity bits,
#returns result as vector
def encodemessage(message):
  #turns the message into a column vector
  vectorlist = []
  for i in range(4):
    vectorlist.append([int(message[i])])
  vector = matrix(vectorlist)
  #encodes with the encode matrix
  vector_with_paritybits = G*vector
  return vector_with_paritybits.getbinary()

#boodschap = input('Vul hier je boodschap in: ')
#boodschapbinair = map(bin, bytearray(boodschap, 'utf8'))

