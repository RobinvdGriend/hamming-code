from matrix import Matrix
from hamming import encodeentiremessage, repairentiremessage, destroyallparitybits
from strconv import str_to_codelist, codelist_to_str, binary_to_codelist
from errormaker import errormaker, errormakerstring

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
    matrixlist = repairentiremessage(matrixlist)
    matrixlistnoparity = destroyallparitybits(matrixlist)
    matrixlistnoparity2 = []
    for matrix in matrixlistnoparity:
        matrixlistnoparity2.append(matrix.transpose())
    answer = codelist_to_str(matrixlistnoparity2)
    return answer


print('Welkom bij de Hammingcode encoderen/decoderen machine.')

def auxilaryprogram():
    input3 = input('Wilt u verder gaan? Type j voor ja, en n voor nee. ')
    if input3 == 'j':
        finalprogram()
    elif input3 != 'n':
        print('Je moet wel een j of n invullen.')
        print('')
        auxilaryprogram()

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


