#!/usr/bin/python3

'''
@cryptopals: s1_c4
@author: Rahil Arora
'''

import binascii

ciphers = [line[:-1] if line[-1] == '\n' else line for line in open('ciphers.txt')]

'''
Returns the numner of times common characters appear in the string
'''
def stupid_score(sentence):
    score = 0
    score = score + sentence.count(' ') + sentence.count('e') + sentence.count('t') + sentence.count('a') + sentence.count('o') + sentence.count('i') + sentence.count('E') + sentence.count('T') + sentence.count('A') + sentence.count('O') + sentence.count('I')
    return score

if __name__ == "__main__":
    high = 0
    i = 1
    correct_key = ' '
    for cipher in ciphers:
        cipher_bytes = binascii.unhexlify(cipher)
        for key in range(0, 256):
            s = ''.join(chr(key ^ k) for k in cipher_bytes)
            ss = stupid_score(s)
            if high < ss:
                high = ss
                correct_key = key
                correct_cipher = s
    print("----------------FOUND----------------")
    print("High =", high)
    print("Key = ", correct_key)
    message = correct_cipher
    print("Message = ", message.encode('utf-8'))
