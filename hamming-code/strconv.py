from matrix import Matrix

def str_to_codelist(string):
    #Bytes are collections of 4 bits in this case
    codelist = []

    bytelist = bytearray(string, 'ascii')

    #For every letter removes b from the string
    for byte in bytelist:
        code = [int(x) for x in list(bin(byte)[2:].zfill(8))]
        codelist.append(Matrix([code[:4]]))
        codelist.append(Matrix([code[4:]]))
    return codelist
