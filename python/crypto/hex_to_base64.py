#!/usr/bin/python3

'''
@author: Rahil Arora
'''

import sys
import base64

def convert(hex_string):
    b = bytes.fromhex(hex_string)
    encoded_bytes = base64.b64encode(b)
    return encoded_bytes

if __name__ == "__main__":
    h = input("Enter the hex value: ")
    e_s = convert(h)
    print(e_s.decode("utf-8"))
