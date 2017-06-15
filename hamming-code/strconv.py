from matrix import Matrix


def str_to_codelist(string):
    # Bytes are collections of 4 bits in this case
    codelist = []

    bytelist = bytearray(string, 'ascii')

    # For every letter removes b from the string
    for byte in bytelist:
        code = [int(x) for x in list(bin(byte)[2:].zfill(8))]
        codelist.append(Matrix([code[:4]]))
        codelist.append(Matrix([code[4:]]))
    return codelist


def codelist_to_str(codelist):
    # A codelist is a list of codes, a code being a 4 bit byte
    chars = []

    # A character is 2 bytes, thus we need every 2 bytes
    # in the codelist, a left one and a right one. Also notice
    # the horrid interface of Matrix() where you need to use .values[0]
    # on every matrix to get something usable

    code_pairs = [(codelist[i].values[0], codelist[i + 1].values[0])
                  for i in range(0, len(codelist) - 1, 2)]

    for lcode, rcode in code_pairs:
        bits = lcode + rcode
        chars.append(chr(int(''.join([str(bit) for bit in bits]), 2)))
    return "".join(chars)
