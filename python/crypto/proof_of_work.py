#!/usr/bin/python3

'''
@author: Rahil Arora
@contact: rahil@jhu.edu
'''

import hashlib
import binascii

last_block = '000000006c0dc12b299db5a5d34168f6a20c3752e02ecf9ec9ac9327d5545310'
name = b'Arora Rahil'
name_hex = (binascii.hexlify(name)).decode('utf-8')
final_string = last_block+name_hex
for nonce in range(0x00000000,0xffffffff):
    nstr = "00000000"+str(hex(nonce))[2:]
    nonce_string = nstr[-8:]
    proof_of_work = hashlib.sha256(((final_string+nonce_string)).encode('utf-8')).hexdigest()
    if proof_of_work[0:8] == "00000000":
        print(proof_of_work)
        print(nonce_string)
        break 
