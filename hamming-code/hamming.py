from matrix import Matrix
import strconv

#The encoding matrix
encoding_matrix = Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1]
    ])


#generating matrix
generator_matrix = encoding_matrix.transpose()

#checking matrix
checking_matrix = Matrix([
  [0, 0, 0, 1, 1, 1, 1],
  [1, 1, 0, 0, 0, 1, 1],
  [1, 0, 1, 0, 1, 0, 1]
  ])

#Takes binary vector of length 4 and adds the parity bits
#Returns result as vector
def encodemessage(message):
  vector_with_paritybits = encoding_matrix*(message.transpose())
  return vector_with_paritybits.getbinary()

#repairs message, may not work, can't test it yet 
#Takes a matrix
def repairmessage(message):
  vector = (checking_matrix*message).getbinary()
  print(vector)
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
    for i in range(len((vector.values))):
      counter += vector.values[i][0] * 2 ** i
  else:
    #in this case checker = True, so it returns the message
    return message
  print(counter)

  new_message = message.values
  #fixes the message
  if counter == 3:
    if new_message[0][0] == 0:
      new_message[0][0] = 1
    else:
      new_message[1][0] = 0
  elif counter == 1:
    if new_message[2][0] == 0:
      new_message[2][0] = 1
    else:
      new_message[2][0] = 0
  elif new_message[counter - 1][0] == 0:
    new_message[counter - 1][0] = 1
  else:
    new_message[counter - 1][0] = 0
  return Matrix(new_message)
  
#Example:
#print(boodschapbinair)
#testvector = Matrix([[1, 0, 1, 1]])
#print(repairmessage(encodemessage(testvector)))

#convertedmessage = str_to_codelist(messagebinary)
#checkedmessage = repairmessage(convertedmessage)
#print(codelist_to_str(checkedmessage))

#adds paritybits to entire message
def encodeentiremessage(message):
    new_list = []
    for matrix in message:
      new_list.append(encodemessage(matrix))
    return new_list

#repairs entire message    
def repairentiremessage(message):
    new_list = []
    for matrix in message:
      new_list.append(repairmessage(matrix))
    return new_list      

hallobinary = strconv.str_to_codelist('hallo')
halloencoded = encodeentiremessage(hallobinary)
for matrix in halloencoded:
  print(matrix)
hallowrong = [
  Matrix([[0], [1], [1], [1], [1], [1], [0]]),
  Matrix([[0], [0], [0], [0], [0], [1], [0]]),
  Matrix([[1], [1], [1], [0], [1], [1], [0]]),
  Matrix([[1], [0], [0], [1], [1], [1], [1]]),
  Matrix([[1], [1], [1], [0], [1], [1], [0]]),
  Matrix([[0], [1], [0], [0], [0], [1], [1]]),
  Matrix([[1], [1], [1], [0], [1], [1], [0]]),
  Matrix([[0], [1], [0], [0], [0], [1], [1]]),
  Matrix([[1], [1], [1], [0], [1], [1], [0]]),
  Matrix([[0], [1], [1], [1], [1], [1], [1]])
]
hallomayberight = repairentiremessage(hallowrong)

print('\n')

for matrix in hallomayberight:
  print(matrix)
