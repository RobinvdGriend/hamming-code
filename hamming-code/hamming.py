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

#repairs message, may not work, can't test it yet 
def repairmessage(message):
  vector = checking_matrix*message
  checker = True
  for element in vector.values[0]:
    if element == 1:
      checker = False
  if checker == False:
    counter = 0
    for i, element enumerate(vector.values[0]):
      counter += element * 2 ** i
  else:
    return vector
  new_message = message.values[0]
  if new_message[counter - 1] == 0:
    new_message[counter - 1] = 1
  else:
    new_message[counter - 1] = 0
  return Matrix(new_message)
  
  

#Example:
boodschap = input('Vul hier je boodschap in: ')
boodschapbinair = list(map(bin, bytearray(boodschap, 'utf8')))
print(boodschapbinair)
testvector = Matrix([[1, 0, 1, 1]])
print(repairmessage(encodemessage(testvector)))
