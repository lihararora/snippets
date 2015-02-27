#!/usr/bin/python3

'''
@cryptopals: s1_c6
@author: Rahil Arora
'''

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    print(bin(ord(s1[0])))
    d = 0
    for ch1, ch2 in zip(s1, s2):
        d = d + bin(ord(ch1) ^ ord(ch2)).count('1')
    return d

if __name__ == "__main__":
    a = hamming_distance('this is a test', 'wokka wokka!!!')
    print(a)
