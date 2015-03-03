#!/usr/bin/python3

'''
@cryptopals: s1_c8
@description: detect_aes_ecb
@author: Rahil Arora
'''

import binascii

ciphers = [line[:-1] if line[-1] == '\n' else line for line in open('challenge8.txt')]

'''
Returns the numner of times common characters appear in the string
'''
def stupid_score(sentence):
    score = 0
    score = score + sentence.count(' ') + sentence.count('e') + sentence.count('t') + sentence.count('a') + sentence.count('o') + sentence.count('i') + sentence.count('E') + sentence.count('T') + sentence.count('A') + sentence.count('O') + sentence.count('I')
    return score

if __name__ == "__main__":
    cipher_bytes = [binascii.unhexlify(c) for c in ciphers]
    encrypted = None
    for cb in cipher_bytes:
        i = 0
        count = 0
        for c in cb:
            '''
            Count number of repeating 16 byte ciphertext blocks in a given ciphertext
            '''
            if i < (len(cb) - 16):
                count = cb.count(cb[i:i+16])
            i = i + 1
            if(count > 1):
                encrypted = cb
    if encrypted != None:
        print("AES ECB encrypted text: ", binascii.hexlify(encrypted))
