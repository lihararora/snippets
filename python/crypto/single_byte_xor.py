#!/usr/bin/python3

'''
@cryptopals: s1_c3
@author: Rahil Arora
'''

import binascii

'''
Returns the numner of times common characters appear in the string
'''
def stupid_score(sentence):
    score = 0
    score = score + sentence.count(' ') + sentence.count('e') + sentence.count('t') + sentence.count('a') + sentence.count('o') + sentence.count('i') + sentence.count('E') + sentence.count('T') + sentence.count('A') + sentence.count('O') + sentence.count('I')
    return score

def detect(cipher_text_bytes):    
    high = 0
    correct_key = ' '
    for key in range(0, 256):
        s = ''.join(chr(key ^ k) for k in cipher_text_bytes)
        ss = stupid_score(s)
        if high < ss:
            high = ss
            correct_key = key
            message = s
    return correct_key

if __name__ == "__main__":
    cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    cipher_text_bytes = binascii.unhexlify(cipher_text)
    cipher_text_string = cipher_text_bytes.decode("utf-8")
    ck = detect(cipher_text_bytes)
    print("----------------FOUND----------------")
    print("Key = ", ck)
    m = ''.join(chr(ck ^ k) for k in cipher_text_bytes)
    print("Message = ", m.encode('utf-8'))
