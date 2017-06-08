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
  vector_with_paritybits = encoding_matrix*(message.transpose())
  return Matrix(vector_with_paritybits.getbinary())

#repairs message, may not work, can't test it yet 
#Takes a matrix
def repairmessage(message):
  vector = checking_matrix*message
  checker = True
  #checks if the return vector is the zero vector. If this is the case
  #checker = True, and there is no mistake
  for element in vector.values[0]:
    if element == 1:
      checker = False
  if checker == False:
    #finds out at what position the mistake is and saves it as
    #counter
    counter = 0
    for i, element in enumerate(vector.values[0]):
      counter += element * 2 ** i
  else:
    #in this case checker = True, so it returns the message
    return message
  new_message = message.values[0]
  #fixes the message
  if new_message[counter - 1] == 0:
    new_message[counter - 1] = 1
  else:
    new_message[counter - 1] = 0
  return Matrix(new_message)
  
#Example:
#boodschap = input('Vul hier je boodschap in: ')
#testvector = Matrix([[1, 0, 1, 1]])
#print(repairmessage(encodemessage(testvector)))
