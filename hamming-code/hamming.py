import random
import math

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
<<<<<<< HEAD
#boodschapbinair = list(map(bin, bytearray(boodschap, 'utf8')))
testvector = Matrix([[1, 0, 1, 1]])
print(checkmessage(encodemessage(testvector)))
=======
#boodschapbinair = map(bin, bytearray(boodschap, 'utf8'))

#Takes a number n, rounds it down to the greatest multiple of 4
#and generates a random list of that many bits
def random_bytes(n):
    bits = [random.choice([0,1]) for i in range(n)]
    return [bits[k:k+4] for k in range(math.floor(len(bits)/4))]

    
>>>>>>> e729978bdf6ffd2a862af71751bbd6ac445db070
