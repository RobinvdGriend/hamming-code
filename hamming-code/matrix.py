class Matrix:
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
    return Matrix(new_matrix)

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

def test_import():
    print("jep")
