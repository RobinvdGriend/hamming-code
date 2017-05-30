class matrix:

  def __init__(self, values):
    self.values = values
    
  def element(self, row, column):
    return self.values[row - 1][column - 1]
    
  def __str__(self):
    return self.values
    
