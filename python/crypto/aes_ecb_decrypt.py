#!/usr/bin/python3

'''
@cryptopals: s1_c7
@author: Rahil Arora
'''

import base64
from Crypto.Cipher import AES

def decrypt(ct, k):
    cipher = AES.new(k, AES.MODE_ECB)
    pt = cipher.decrypt(ct)
    return pt

if __name__ == "__main__":
    text = open("challenge7.txt").read()
    cipher_bytes = base64.b64decode(text)
    message = decrypt(cipher_bytes, 'YELLOW SUBMARINE')
    print(message)
