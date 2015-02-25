#!/usr/bin/python3

'''
@cryptopals: s1_c4
@author: Rahil Arora
'''

import binascii

ciphers = []
ciphers = [line for line in open('ciphers.txt', "rb")]
print(ciphers)

'''
Returns the numner of times common characters appear in the string
'''
def stupid_score(sentence):
    score = 0
    score = score + sentence.count(' ') + sentence.count('e') + sentence.count('t') + sentence.count('a') + sentence.count('o') + sentence.count('i') + sentence.count('E') + sentence.count('T') + sentence.count('A') + sentence.count('O') + sentence.count('I')
    return score

if __name__ == "__main__":
    key_chain = " ETAOINSHRDLUCMFGYPWBVVKXJQZetaoinshrdlucmfgypwbvkxjqz"
    for hex_bytes in ciphers:
        cipher = binascii.hexlify(hex_bytes)
        high = 0
        correct_key = ' '
        cipher_string = cipher_bytes.decode("utf-8").rstrip('\n')
        print(cipher_string)
        for key in key_chain:
            s = ''.join(chr(ord(key) ^ ord(k)) for k in cipher_string)
            ss = stupid_score(s)
            if high < ss:
                high = ss
                correct_key = key
        #print("----------------FOUND----------------")
        #print("High =", high)
        #print("Key = ", correct_key)
        #message = ''.join(chr(ord(correct_key) ^ ord(k)) for k in cipher_string)
        #print("Message = ", message)
