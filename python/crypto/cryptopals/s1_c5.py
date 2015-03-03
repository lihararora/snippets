#!/usr/bin/python3

'''
@cryptopals: s1_c5
@author: Rahil Arora
'''

import binascii

def xor(text, key):
    text_bytes = text.encode('utf-8')
    key_bytes = key.encode('utf-8')
    i = 0
    x = ''
    if len(text) < len(key):
        i = 0
        x = ''
        for t in text_bytes:
            x = x.join(chr(key_bytes[i] ^ t))
            i = i + 1 
    else:
        i = 0
        x = ''
        for t in text_bytes:
            x = x + chr(key_bytes[i%len(key_bytes)] ^ t)
            i = i + 1 
    return binascii.hexlify(x.encode('utf-8'))

if __name__ == '__main__':
    t = open("challenge5.txt").read()
    print("Reading message from the file 'challenges.txt'")
    k = input("Enter the key: ")
    x = xor(t, k)
    print("Xored message: ", x.decode('utf-8'))
