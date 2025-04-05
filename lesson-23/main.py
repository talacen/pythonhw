def decrypt_cezar(ciphertext: str, key: int, alphabet: str = 'abcdefghijklmnopqrstuvwxyz') -> str:
    decryptedtxt = []
    loweralp = alphabet.lower()
    upperalp = alphabet.upper()
    
    for char in ciphertext:
        if char in upperalp:
            index = (upperalp.index(char) - key) % len(alphabet)
            decrypted_char = upperalp[index]
            decryptedtxt.append(decrypted_char)
        elif char in loweralp:
            index = (loweralp.index(char) - key) % len(alphabet)
            decrypted_char = loweralp[index]
            decryptedtxt.append(decrypted_char)
        else:
            decryptedtxt.append(char)
    return ''.join(decryptedtxt)

print(decrypt_cezar('hello world', 3))