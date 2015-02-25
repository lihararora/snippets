#!/usr/bin/python3

'''
@author: Rahil Arora
'''

import binascii

cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
cipher_bytes = binascii.unhexlify(cipher)
cipher_string = cipher_bytes.decode("utf-8")
key_chain = " ETAOINSHRDLUCMFGYPWBVVKXJQZetaoinshrdlucmfgypwbvkxjqz"

'''
Returns the numner of times common characters appear in the string
'''
def stupid_score(sentence):
    score = 0
    score = score + sentence.count(' ') + sentence.count('e') + sentence.count('t') + sentence.count('a') + sentence.count('o') + sentence.count('i') + sentence.count('E') + sentence.count('T') + sentence.count('A') + sentence.count('O') + sentence.count('I')
    return score

if __name__ == "__main__":
    high = 0
    correct_key = ' '
    for key in key_chain:
        s = ''.join(chr(ord(key) ^ ord(k)) for k in cipher_string)
        ss = stupid_score(s)
        if high < ss:
            high = ss
            correct_key = key
    print("----------------FOUND----------------")
    print("Key = ", correct_key)
    message = ''.join(chr(ord(correct_key) ^ ord(k)) for k in cipher_string)
    print("Message = ", message)
