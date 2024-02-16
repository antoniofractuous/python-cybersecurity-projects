def decrypt(ciphertext, distance):
    result = ''
    for lt in ciphertext:
        if lt.islower():
            result += chr((ord(lt) - distance - ord('a')) % 26 + ord('a'))
        elif lt.isalpha():
            result += chr((ord(lt) - distance - ord('A')) % 26 + ord('A'))
        else:
            result += lt
    return result

def decrypt_cipher(cipher):
    for rot in range(1, 26):
        cipher_decrypt = decrypt(cipher, rot)
        print(f'Rot {rot}: {cipher_decrypt}')

cipher_text = input('cipher text: ')
decrypt_cipher(cipher_text)