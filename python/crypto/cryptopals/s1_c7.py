#!/usr/bin/python3

'''
@cryptopals: s1_c7
@description: aes_ecb
@author: Rahil Arora
'''

import base64
from Crypto.Cipher import AES

def decrypt(ct, k):
    cipher_text = AES.new(k, AES.MODE_ECB)
    pt = cipher_text.decrypt(ct)
    return pt

if __name__ == "__main__":
    text = open("challenge7.txt").read()
    cipher_text_bytes = base64.b64decode(text)
    message = decrypt(cipher_text_bytes, 'YELLOW SUBMARINE')
    print(message)
