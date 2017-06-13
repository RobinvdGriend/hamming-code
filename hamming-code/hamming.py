from matrix import Matrix
import strconv
from copy import deepcopy

#Generator matrix
generator_matrix = Matrix([
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
    ])

#parity-check matrix
parity_check_matrix = Matrix([
  [1, 0, 1, 0, 1, 0, 1],
  [0, 1, 1, 0, 0, 1, 1],
  [0, 0, 0, 1, 1, 1, 1]
  ])

#Takes binary vector of length 4 and adds the parity bits
#Returns result as vector
def encodemessage(message):
  vector_with_paritybits = generator_matrix*(message.transpose())
  return vector_with_paritybits.getbinary()

#repairs message, may not work, can't test it yet 
#Takes a matrix
def repairmessage(message):
  vector = (parity_check_matrix*message).getbinary()
  checker = True
  #checks if the return vector is the zero vector. If this is the case
  #checker = True, and there is no mistake
  for i in range(len(vector.values)):
    if vector.values[i][0] == 1:
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
  new_message = message.values
  #fixes the message
  if new_message[counter - 1][0] == 0:
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

#takes a 7x1 vector, destroys the parity bits and returns
#what is left
def destroyparitybits(message):
  new_message = message.values
  del new_message[0]
  del new_message[0]
  del new_message[1]
  return Matrix(new_message)

def destroyallparitybits(message):
    new_list = []
    for matrix in message:
      new_list.append(destroyparitybits(matrix))
    return new_list 

#TESTCASE
hallobinary = strconv.str_to_codelist('hallo')
halloencoded = encodeentiremessage(hallobinary)

#print helloencoded
print('De gecodeerde matrix: ')
for matrix in halloencoded:
  print(matrix)

#de verkeerde matrix (in rij i zit de i'de bit fout voor 0 < i < 8)
hallowrong = [
  Matrix([[0], [1], [0], [0], [1], [1], [0]]),
  Matrix([[1], [0], [1], [0], [0], [0], [0]]),
  Matrix([[1], [1], [1], [0], [1], [1], [0]]),
  Matrix([[1], [1], [0], [0], [0], [0], [1]]),
  Matrix([[1], [1], [0], [0], [0], [1], [0]]),
  Matrix([[0], [1], [1], [1], [1], [1], [0]]),
  Matrix([[1], [1], [0], [0], [1], [1], [1]]),
  Matrix([[0], [1], [1], [1], [1], [0], [0]]),
  Matrix([[1], [1], [0], [0], [1], [1], [0]]),
  Matrix([[1], [1], [1], [1], [1], [1], [1]])
]
#de gerepareerde matrix
hallomayberight = repairentiremessage(hallowrong)

hallomayberightgaikslopen = deepcopy(hallomayberight)

#de gerepareerde matrix zonder paritybits
hallomayberightwithoutparitybits = destroyallparitybits(hallomayberightgaikslopen)


print('\n')

print('De gerepareerde matrix: ')



for matrix in hallomayberight:
  print(matrix)

print('\n')

print('Zonder parity bits: ')


for matrix in hallomayberightwithoutparitybits:
  print(matrix)


