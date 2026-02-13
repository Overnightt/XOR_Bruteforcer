
#XOR data with a repeating key.
def XOR_bytes(data: bytes,key: bytes):
    new_data = []
    for i in range (len(data)):
        key_index = i % len(key)
        new_byte = data[i]^key[key_index]
        new_data.append(new_byte)
    return bytes(new_data)

#Parse partial key with ? for unknown bytes
def parse_key(key:str):
    unknown = []
    known = {}
    for i in range (len(key)):
        if key[i] == "?":
            unknown.append(i)
        else:
            known[i] = ord(key[i])
    return known, unknown

#Score decrypted data based on printable characters.Higher score = more likely to be readable text
def score_txt(data: bytes):
    score = 0
    for i in range (len(data)):
        if 32 <= data[i] <= 126:
            score += 1
    return score