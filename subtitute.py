from string import ascii_letters

cipher_letters = 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'
trans = str.maketrans(ascii_letters, cipher_letters)

trans_rev = str.maketrans(cipher_letters, ascii_letters)

text_to_cipher = input('Text to cipher: ')

ciphered = text_to_cipher.translate(trans)
plaint = ciphered.translate(trans_rev)
print(f'Ciphered text: {ciphered}')
print(f'plain tex: {plaint}')