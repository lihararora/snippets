#!/usr/bin/python3

'''
@cryptopals: s1_c2
@description: fixed_xor
@author: Rahil Arora
'''

import binascii

def xor(input1, input2):
    binary_input1 = bytes.fromhex(input1)
    binary_input2 = bytes.fromhex(input2)
    #print(binary_input1)
    #print(binary_input2)
    xored_string = ''.join(chr(a ^ b) for a, b in zip(binary_input1, binary_input2))
    xored_bytes = bytes(xored_string, encoding='UTF-8')
    return xored_bytes

if __name__ == "__main__":
    input1 = input("Enter first hex string: ")
    input2 = input("Enter second hex string: ")
    xb = xor(input1, input2)
    xored_hex = binascii.hexlify(xb)
    print(xored_hex.decode('UTF-8'))
