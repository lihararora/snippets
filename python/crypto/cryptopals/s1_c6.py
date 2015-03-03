#!/usr/bin/python3

'''
@cryptopals: s1_c6
@description: break_repeating_xor
@author: Rahil Arora
'''

import binascii
import string
import base64
import s1_c3 as SBX
import s1_c5 as RKX

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    d = 0
    for ch1, ch2 in zip(s1, s2):
        d = d + bin(ch1 ^ ch2).count('1')
    return d

def find_key_size(text):
    normalized_hamming = {}
    for size in range(2, 40):
        b1 = text[0:size-1]
        b2 = text[size:2*size-1]
        b3 = text[2*size:3*size-1]
        b4 = text[3*size:4*size-1]
        h1 = hamming_distance(b1, b2)
        h2 = hamming_distance(b2, b3)
        h3 = hamming_distance(b3, b4)
        normalized_hamming[size] = ((h1+h2+h3)/size)/3
    return sorted(normalized_hamming.items(), key=lambda x: x[1])

def is_printable(s):
    return all(c in string.printable for c in s)

def nested_list(l, s):
    new_list = [s[i:i+l] for i in range(0, len(s), l)]
    return new_list

def find_key(cipher_text_bytes):
    key = ""
    key_size = 0
    d = find_key_size(cipher_text_bytes)
    for size, distance in d:
        cipher_text_list = cipher_text_bytes
        ll = nested_list(size, cipher_text_bytes)
        block = bytearray()
        for b in ll:
            block.append(b[0])
        key_part = SBX.detect(block)
        x1 = ''.join(chr(key_part ^ k) for k in block)
        if is_printable(x1):
            key_size = size
            key = key + chr(key_part)
            for i in range(1, key_size):
                block = bytearray()
                for b in ll:
                    try:
                        block.append(b[i])
                    except IndexError:
                        break
                key_part = SBX.detect(block)
                x1 = ''.join(chr(key_part ^ k) for k in block)
                if is_printable(x1):
                    key = key + chr(key_part)
    return key


if __name__ == "__main__":
    s = open('challenge6.txt').read()
    cipher_text_bytes = base64.b64decode(s)
    key = find_key(cipher_text_bytes)
    print("Key = ", key)
    hex_message = RKX.xor(cipher_text_bytes.decode('utf-8'), key)
    actual_message = binascii.unhexlify(hex_message)
    print("Message = ", actual_message)
