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

#Takes a string with a four 0's or 1's as argument and adds the parity bits
#Returns result as vector
def encodemessage(message):
  #Turns the message into a column vector
  vectorlist = []
  for i in range(4):
    vectorlist.append([int(message[i])])
  vector = Matrix(vectorlist)
  #Encodes with the encode matrix
  vector_with_paritybits = encoding_matrix*vector
  return vector_with_paritybits.getbinary()


def checkmessage(message):
  #Turns the message into a column vector
  vectorlist = []
  for i in range(4):
    vectorlist.append([int(message[i])])
  vector = Matrix(vectorlist)
  #Encodes with the encode matrix
  vector_with_paritybits = checking_matrix*vector
  return vector_with_paritybits.getbinary()


#Example:
#boodschap = input('Vul hier je boodschap in: ')
#boodschapbinair = map(bin, bytearray(boodschap, 'utf8'))

