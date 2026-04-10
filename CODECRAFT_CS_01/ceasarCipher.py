small_alphabets = 'abcdefghijklmnopqrstuvwxyz'
cap_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    cipherText = ''
    for letter in text:
        if not letter == ' ':
            if ord(letter)>=65 and ord(letter)<=90:
                index = cap_alphabets.find(letter)
                new_index = index + key
                if new_index>=26:
                    new_index -= 26
                cipherText += cap_alphabets[new_index]
            elif ord(letter)>=97 and ord(letter)<=122:
                index = small_alphabets.find(letter)
                new_index = index + key
                if new_index>=26:
                    new_index -= 26
                cipherText += small_alphabets[new_index]
            else:
                cipherText += letter
    return cipherText

def decrypt(text, key):
    plainText = ''
    for letter in text:
        if not letter == ' ':
            if ord(letter)>=65 and ord(letter)<=90:
                index = cap_alphabets.find(letter)
                new_index = index - key
                if new_index>=26:
                    new_index += 26
                plainText += cap_alphabets[new_index]
            elif ord(letter)>=97 and ord(letter)<=122:
                index = small_alphabets.find(letter)
                new_index = index - key
                if new_index>=26:
                    new_index += 26
                plainText += small_alphabets[new_index]
            else:
                plainText += letter
    return plainText

print('*****Ceasar Cipher*****')

mode = input('Enter Mode (e/d): ')

if mode=='e':
    print("Encryption Mode Enabled.")
    text = input('Enter text to be encrypted: ')
    key = int(input('Enter key: '))
    result = encrypt(text, key)
    print(f'Cipher Text: {result}')
elif mode=='d':
    print("Decryption Mode Enabled.")
    text = input('Enter text to be decrypted: ')
    key = int(input('Enter key: '))
    result = decrypt(text, key)
    print(f'Plain Text: {result}')
