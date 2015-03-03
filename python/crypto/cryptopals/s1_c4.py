#!/usr/bin/python3

'''
@cryptopals: s1_c4
@author: Rahil Arora
'''

import binascii

cipher_text_texts = [line[:-1] if line[-1] == '\n' else line for line in open('challenge4.txt')]

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
    for cipher_text in cipher_text_texts:
        cipher_text_bytes = binascii.unhexlify(cipher_text)
        for key in range(0, 256):
            s = ''.join(chr(key ^ k) for k in cipher_text_bytes)
            ss = stupid_score(s)
            if high < ss:
                high = ss
                correct_key = key
                correct_cipher_text = s
    print("----------------FOUND----------------")
    print("High =", high)
    print("Key = ", correct_key)
    message = correct_cipher_text
    print("Message = ", message.encode('utf-8'))
