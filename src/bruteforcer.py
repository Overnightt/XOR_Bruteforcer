from itertools import product

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
    frequent_letters = b'etaoinshrlETAOINSHRL' #the most frequent letters in english
    for i in range (len(data)):
        if data[i] in frequent_letters:
            score +=3
        elif 97 <= data[i] <= 122:  
            score += 2
        elif 65 <= data[i] <= 90:
            score += 2
        elif data[i] == 32: 
            score += 2
        elif 32 <= data[i] <= 126:
            score += 1
        else:
            score -= 2
    return score

#generates all possible keys
def generate_keys(known: dict, unknown: list, key_length: int):
    possible_keys=[]
    for combination in product(range(256), repeat=len(unknown)):
        key = [0]*key_length
        for position, value in known.items():
            key[position] = value
        for i, position in enumerate(unknown):
            key[position] = combination[i]
        possible_keys.append(bytes(key))
    return possible_keys

#The main bruteforcer function
def bruteforcer(encrypted_data: bytes, known: dict, unknown:list, key_length: int, n_solutions: int=3):
    solutions = []
    possible_keys = generate_keys(known, unknown, key_length)
    for key in possible_keys:
        decrypted_data = XOR_bytes(encrypted_data, key)
        score = score_txt(decrypted_data) 
        solutions.append((key, decrypted_data, score))
    solutions.sort(key=lambda x: x[2], reverse = True)
    return solutions[:n_solutions]
