from matrix import Matrix
from strconv import str_to_codelist, codelist_to_str, binary_to_codelist
from errormaker import errormakerstring


'''
Chooses to import either the 7,4 or 8,4 variant of a function
'''

begin = input('Voor 7,4 Hammingcode typ 7, voor 8,4 Hammingcode typ 8. ')
if begin == '7':
    from hamming74 import encodeentiremessage, repairentiremessage, destroyallparitybits, length
if begin == '8':
    from hamming84 import encodeentiremessage, repairentiremessage, destroyallparitybits, length

'''
Takes a string as argument, returns the binary representation with paritybits.
'''
def encoderen(message):
    string = ''
    matrixlist = str_to_codelist(message)
    paritymatrixlist = encodeentiremessage(matrixlist)
    for matrix in paritymatrixlist:
        for i in range(length):
            string += str(matrix.values[i][0])
    return string


'''
Takes a string of 1 and 0's as argument, gives the option to make a mistake,
then repairs the string, removes the parity bits, and translates it back into
a normal string, which was the original message
'''
def decoderen(message):
    input1 = input('Wilt u random 1 bits fouten aanbrengen om het bericht te laten herstellen? Type j voor ja, en n voor nee.')
    if input1 != 'j' and input1 != 'n':
        print('Je moet wel een j of n invullen.')
        print('')
    elif input1 == 'j':
        message = errormakerstring(message, length)
        print('')
        print('Dit is het bericht met 1 bitsfouten:', message)
        matrixlist = binary_to_codelist(message, length)
        matrixlist = repairentiremessage(matrixlist)
        matrixlistnoparity = destroyallparitybits(matrixlist)
        matrixlistnoparity2 = []
        for matrix in matrixlistnoparity:
            matrixlistnoparity2.append(matrix.transpose())
        answer = codelist_to_str(matrixlistnoparity2)
        print('')
        print('De code is hersteld en vertaald naar:')
        return answer
    elif input1 == 'n':
        matrixlist2 = binary_to_codelist(message, length)
        matrixlist = repairentiremessage(matrixlist2)
        if matrixlist != matrixlist2:
            print('We hebben een fout gecorrigeerd')
        matrixlistnoparity = destroyallparitybits(matrixlist)
        matrixlistnoparity2 = []
        for matrix in matrixlistnoparity:
            matrixlistnoparity2.append(matrix.transpose())
        answer = codelist_to_str(matrixlistnoparity2)
        return answer

print('')
print('Welkom bij de Hammingcode',begin,',4 encoderen/decoderen machine.')


'''
Is used to continue the program if necessary
'''
def auxilaryprogram():
    input3 = input('Wilt u verder gaan? Type j voor ja, en n voor nee. ')
    if input3 == 'j':
        finalprogram()
    elif input3 != 'n':
        print('Je moet wel een j of n invullen.')
        print('')
        auxilaryprogram()


'''
This is the final interface program that allows the user to either encode
or decode their message. Also includes the option to continue encoding or
decoding if the user forgot a part of the message. The user will insert
the entire message in one go, the recursion is just a fail safe in
case the user forgot something, so the odds
of the recursive depth being exceeded are infinitesimal.
'''
def finalprogram():
    input1 = input('Wilt  u encoderen of decoderen? Type e voor encoderen en d voor decoderen. ')
    if input1 != 'e' and input1 != 'd':
        print('Je moet wel een e of d invullen.')
        print('')
        finalprogram()
    input2 = input('Vul hier uw boodschap in: ')
    if input1 == 'e':
        print(encoderen(input2))
    else:
        print(decoderen(input2))
    auxilaryprogram()


finalprogram()


