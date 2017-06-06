from matrix import Matrix

#The encoding matrix
encoding_matrix = Matrix([
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
    ])

#The parity checking matrix
checking_matrix = Matrix([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 1, 0, 0, 1, 1],
  [0, 0, 0, 1, 1, 1, 1]
  ])

#Takes binary vector of length 4 and adds the parity bits
#Returns result as vector
def encodemessage(message):
  print(message.transpose())
  vector_with_paritybits = encoding_matrix*(message.transpose())
  return Matrix(vector_with_paritybits.getbinary())

#returns true if the message is not corrupted, returns false if message is
#corrupted. To be implemented: repairing the message if there is a mistake
def checkmessage(message):
  vector = checking_matrix*message
  checker = True
  for element in vector.values[0]:
    if element == 1:
      checker = False
  return checker
   
#Example:
#boodschap = input('Vul hier je boodschap in: ')
#boodschapbinair = list(map(bin, bytearray(boodschap, 'utf8')))
testvector = Matrix([[1, 0, 1, 1]])
print(checkmessage(encodemessage(testvector)))
