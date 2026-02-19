# XOR Bruteforcer

A XOR cipher bruteforcer with partial key knowledge support. Designed for CTF challenges and cryptanalysis learning.

Originally created to solve the **W1seGuy challenge on TryHackMe**.

## Features

- **Partial Key Support**: Know part of the key? Use `?` for unknown bytes
- **Smart Scoring**: Uses English letter frequency analysis for accurate results
- **Top Results**: Returns multiple candidates ranked by likelihood
- **CTF-Ready**: Perfect for challenges where you have hints about the XOR key

## Usage

No dependencies required - uses only Python standard library.

```bash
python main.py
```

### Example Session
```
=== XOR BRUTEFORCER ===

Enter message to decrypt (hexadecimal): 33232d252d2e612f263231222627
Please enter the key length: 3
Please enter the key, enter unknown characters as ?: AB?

Bruteforcing...
```

## How It Works

1. **Parse Partial Key**: Separates known bytes from positions to bruteforce
2. **Generate Keys**: Creates all possible key combinations (256^n where n = unknown bytes)
3. **XOR Decrypt**: Tests each key against the encrypted data
4. **Smart Scoring**: Ranks results using:
   - Bonus for common English letters (e, t, a, o, i, n, s, h, r, l)
   - Bonus for uppercase/lowercase letters and spaces
   - Penalty for non-printable characters

## Project Structure
```
XOR_Bruteforcer/
├── src/
│   └── bruteforcer.py    # Core project logic
├── main.py               # User interface
└── README.md
```

## Algorithm Complexity

- **Single unknown byte**: 256 attempts
- **Two unknown bytes**: 65,536 attempts 
- **Three unknown bytes**: 16,777,216 attempts 

Performance depends on message length and hardware.

## Use Cases

- **CTF Challenges**: Quickly recover XOR keys with partial knowledge (like W1seGuy on TryHackMe)
- **Cryptanalysis Practice**: Learn about XOR cipher weaknesses
- **Forensics**: Decrypt XOR-encrypted data when you have hints

## Inspiration

This tool was inspired by the **W1seGuy challenge on TryHackMe**, where partial key knowledge can significantly reduce bruteforce complexity.

## Limitations

- Only supports **repeating-key XOR** 
- Key must be in **UTF-8 format** (ASCII characters)
- Encrypted data must be provided in **hexadecimal format**
- Scoring optimized for **English text** (may not work well for other languages)
- Performance degrades with 3+ unknown bytes

## Contributing

Feel free to open issues or submit PRs for improvements.

Built as a learning project to understand XOR encryption and bruteforce techniques.