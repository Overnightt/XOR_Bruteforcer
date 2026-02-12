
def XOR_bytes(data: bytes,key: bytes):
    new_data= []
    for i in range(len(data)):
        key_index= i % len(key)
        new_byte= data[i]^key[key_index]
        new_data.append(new_byte)
    return bytes(new_data)


