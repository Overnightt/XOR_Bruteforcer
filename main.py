from src.bruteforcer import XOR_bytes, parse_key, score_txt,generate_keys, bruteforcer

def main():
    encrypted_data = input("Enter message to decrypt (hexadecimal)")
    encrypted_data = bytes.fromhex(encrypted_data)
    key_length = int(input("please enter the key length"))
    user_key = input ("please enter the key, enter unkno charachters as ?  ")
    known, unknown = parse_key(user_key)
    print("Bruteforcing... \n")
    results = bruteforcer(encrypted_data, known, unknown, key_length)
    for i, (key, decrypted, score) in enumerate(results, 1):
        print(f"#{i}")
        print(f"  Key: {key.decode('latin-1', errors='ignore')}")
        print(f"  Decrypted: {decrypted.decode('utf-8', errors='ignore')}")


if __name__ == "__main__":
    main()