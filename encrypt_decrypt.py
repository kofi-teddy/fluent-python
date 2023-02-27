
from cryptography.fernet import Fernet
 
# # we will be encrypting the below string.
# message = "hello geeks"
 
# # generate a key for encryption and decryption
# # You can use fernet to generate
# # the key or use random key generator
# # here I'm using fernet to generate key
 
# # key = Fernet.generate_key()
# key = b'1l0O5jEZkaj6LguZW3amFgFpO_kCBBN_xv9TucQ1xPs='
# print(key)
 
# # Instance the Fernet class with the key
 
# fernet = Fernet(key)
 
# # then use the Fernet class instance
# # to encrypt the string string must
# # be encoded to byte string before encryption
# encMessage = fernet.encrypt(message.encode())
# encMessage1 = b'gAAAAABj_K51IdYjDDI-987h42hLeYS93jvufIVAjsCJ0GyCe0xKJHdTHN9TqX8D9KDzoZVEMv5RZhBFOcL0ljYOUMTSxd_kMg=='
# # print("original string: ", message)
# print("encrypted string: ", encMessage)
 
# # decrypt the encrypted string with the
# # Fernet instance of the key,
# # that was used for encrypting the string
# # encoded byte string is returned by decrypt method,
# # so decode it to string with decode methods
# decMessage = fernet.decrypt(encMessage).decode()
 
# print("decrypted string: ", decMessage)


# if encMessage == encMessage1:
#     print("yes")
# else:
#     print("no")

# def encrypt_phone_numner(phone) -> str:
#     from cryptography.fernet import Fernet
#     import os

#     ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
#     cipher_suite = Fernet(ENCRYPTION_KEY.encode())


from cryptography.fernet import Fernet
message = "hello geeks"
key = b'1l0O5jEZkaj6LguZW3amFgFpO_kCBBN_xv9TucQ1xPs='
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
encMessage1 = b'gAAAAABj_M1erUvFgv0UruwqBUI2hSmbn4DWXNcP97w9eU2SJHlZ6mSp2I7A60ODlpmsw6txAvWGfWZww2zWokIYxTd-Z4HEpQ=='
print("encrypted string: ", encMessage)

if encMessage == encMessage1:
    print("yes")
else:
    print("no")
