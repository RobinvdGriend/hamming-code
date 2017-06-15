from matrix import Matrix
from hamming import encodeentiremessage, repairentiremessage, destroyallparitybits
from strconv import str_to_codelist, codelist_to_str, binary_to_codelist

print('Welkom bij de Hammingcode encoderen/decoderen machine.')
input1 = input('Wilt  u encoderen of decoderen? Type 1 voor encoderen en 2 voor decoderen')
input2 = input('Vul hier uw boodschap in: ')

if input1 == '1':
    print(encoderen(input2)
elif input == '2':
    print(decoderen(input2)
else:
    print('Je moet wel een 1 of 2 invullen')




def encoderen(message):
    string = ''
    matrixlist = str_to_codelist(message)
    paritymatrixlist = encodeentiremessage(matrixlist)
    for matrix in paritymatrixlist:
        for i in range(7):
            string += str(matrix.values[i][0])
    return string

def decoderen(message):
    matrixlist = binary_to_codelist(message)
    matrixlistnoparity = destroyallparitybits(matrixlist)
    answer = codelist_to_str(matrixlistnoparity)






'''
def message_to_binstring(message):
    bytelist = bytearray(message, 'ascii')
    binstring = ''
    for byte in bytelist:
        for digit in list(bin(byte)[2:].zfill(8)):
            binstring = binstring + digit
    return binstring

def binstring_to_message(binstring):
    message = ''
    while binstring != '':
        #Every letter is represented by 8 1's and 0's, and the value of the binary number is the letter his chr()
        letter = chr(int(binstring[:8], 2))
        message = message + letter
        binstring = binstring[8:]
    return message
    
print(message_to_binstring(message))
print(binstring_to_message(message_to_binstring(message)))
''' 
