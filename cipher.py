# define variables
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'
# define vigenere function with three params
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower(): # .lower change capitale letter to lowercase

        # Append any non-letter character to the message
        if not char.isalpha():  # .isalpha check if is alphabet or not
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}') # f string to print string with varibale inside ' ' with notation {} 
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')


# https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-string-manipulation-by-building-a-cipher/step-95
