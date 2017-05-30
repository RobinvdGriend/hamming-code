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
      
  
  def __str__(self):
    return str(self.values)
  
  
  
  
    
hoi = matrix([[1, 2], [3, 4]])
doei = matrix([[1, 1], [1, 1]])

print(hoi*doei)
