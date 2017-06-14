from matrix import Matrix
print('Vul hier uw boodschap in: ')
message = input()
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
