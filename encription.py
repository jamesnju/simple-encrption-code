import random

msg ="my name is error"
print(msg)
key = ''
encryption_level = 248 // 8 #this the level of encryption, its 31 bye

char_pool = ''

for i in range(0x000, 0xFF):
    char_pool += chr(i)
#print(char_pool)
key = ''
for i in range(encryption_level):      #looping the key 
    key += random.choice(char_pool)
#print(key)#testing the encryption
#print(len(key)) #length of the encryption key  
key_index = 0  #stores index values
max_key_index = encryption_level - 1
encrypted_msg = ''
for char in msg:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_msg += chr(encrypted_char) #returns the original char
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'decrypted message: {encrypted_msg}')

key_index = 0
decrypted_msg = ''
for char in encrypted_msg:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_msg += chr(decrypted_char)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'Decrypted message: {decrypted_msg}')         