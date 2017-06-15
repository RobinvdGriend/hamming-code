from matrix import Matrix

def str_to_codelist(string):
    # Takes an ASCII encoded string, converts it to
    # a list of row matrices with length 4

    codelist = []

    bytelist = bytearray(string, 'ascii')

    # for every letter removes b from the string
    for byte in bytelist:
        code = [int(x) for x in list(bin(byte)[2:].zfill(8))]
        codelist.append(Matrix([code[:4]]))
        codelist.append(Matrix([code[4:]]))
    return codelist


def codelist_to_str(codelist):
    # Takes a list of row matrices and returns the ASCII represtation
    # as a string
    chars = []

    # A character is 2 bytes, thus we need every 2 bytes
    # in the codelist, a left one and a right one. <rant> Also notice
    # the horrid interface of Matrix() where you need to use .values[0]
    # on every matrix to get something usable </rant>

    code_pairs = [(codelist[i].values[0], codelist[i + 1].values[0])
                  for i in range(0, len(codelist) - 1, 2)]

    for lcode, rcode in code_pairs:
        bits = lcode + rcode
        chars.append(chr(int(''.join([str(bit) for bit in bits]), 2)))
    return "".join(chars)

def binary_to_codelist(binarystring,codelength=7):
    # Takes a string of bits (like "1100011") and turns it
    # into a list of row matrices with length codelength
    codelist = []
    
    bytelist = [binarystring[i:i+codelength] for i in range(0,len(binarystring),codelength)]

    for byte in bytelist:
        code = [int(x) for x in list(byte)]
        codelist.append(Matrix([code]))
    return codelist

def codelist_to_binary(codelist):
    # Takes a list of row matrices and returns a string of bits
    # such as "0100111"
    chars = []
    
    for code in codelist:
        bits = code.values[0]
        chars.append(''.join([str(bit) for bit in bits]))
    return "".join(chars)
