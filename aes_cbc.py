'''
@author: Rahil Arora
@contact: rahil@jhu.edu
'''

from os import urandom
from hashlib import sha1
from Crypto.Cipher import AES


sha1_blocksize = sha1().block_size
ipad = chr(0x36) * sha1_blocksize
opad = chr(0x5c) * sha1_blocksize

def hmac_sha1(key_mac, plain):
        if len(key_mac) > sha1_blocksize:
            key_mac = sha1(key_mac).digest()
        key_mac += chr(0) * (sha1_blocksize - len(key_mac))
        i_key_pad = strxor(ipad, key_mac)
        o_key_pad = strxor(opad, key_mac)
        hmac = sha1(o_key_pad + sha1(i_key_pad + plain).digest())
        return hmac.digest()

def strxor(a, b):
        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

class Encrypt:
    
    def __init__(self):
        pass
    
    def padding(self, authentic_plain):
        pad = ""
        n = len(authentic_plain)%16
        if n ==0:
            pad += chr(0x10) * 16
        else:
            num = 16 - n
            pad += chr(num) * num
        return authentic_plain+pad
    
    def enc_aes_cbc(self, key_enc, iv, authentic_padded_plain):
        cipher = ""
        c = ""
        n = len(authentic_padded_plain)/16
        for i in range(0, n):
            block = authentic_padded_plain[i*16:(i+1)*16]
            if(i == 0):
                c = AES.new(key_enc).encrypt(strxor(block, iv))
                cipher += c
            else:    
                c = AES.new(key_enc).encrypt(strxor(block, c))
                cipher += c
        return iv+cipher
    
    def perform_encryption(self, key_enc, key_mac, plain):
        authentic_plain = plain+hmac_sha1(key_mac, plain)
        authentic_padded_plain = self.padding(authentic_plain)
        iv = urandom(16)
        iv_cipher = self.enc_aes_cbc(key_enc, iv, authentic_padded_plain)
        return iv_cipher
        
 
class Decrypt:
    
    def __init__(self):
        pass
    
    def dec_aes_cbc(self, key_enc, iv_cipher):
        iv = iv_cipher[0:16]
        cipher = iv_cipher[16:]
        n = len(cipher)/16
        authentic_padded_plain = ""
        block_prev = ""
        for i in range(0, n):
            block = cipher[i*16:(i+1)*16]
            if(i == 0):
                authentic_padded_plain += strxor(AES.new(key_enc).decrypt(block),iv)
                block_prev = block
            else:    
                authentic_padded_plain += strxor(AES.new(key_enc).decrypt(block),block_prev)
                block_prev = block
        return authentic_padded_plain
        
    def padding_check(self, authentic_padded_plain):
        last_byte = authentic_padded_plain[-1]
        last_byte_int = int(last_byte.encode('hex'), 16)
        pad = last_byte * last_byte_int
        if authentic_padded_plain[-last_byte_int:] == pad:
            return authentic_padded_plain[:-last_byte_int]
        else:
            print "INVALID PADDING"
            return None
        
    def hmac_check(self,authentic_plain, key_mac):
        hmac = authentic_plain[-20:]
        plain = authentic_plain[:-20]
        new_hmac = hmac_sha1(key_mac, plain)
        if new_hmac == hmac:
            return plain
        else:
            print "INVALID MAC!"
            return None
        
    def perform_decryption(self, key_enc, key_mac, iv_cipher):
        authentic_padded_plain = self.dec_aes_cbc(key_enc, iv_cipher)
        authentic_plain = self.padding_check(authentic_padded_plain)
        plain = self.hmac_check(authentic_plain, key_mac)
        return plain
    
    
if __name__ == "__main__":
    
    key_enc = ""
    key_mac = ""
    plain = ""
    iv_cipher = ""
    while len(key_enc) != 16: 
        key_enc = raw_input("Enter Encryption Key (16 bytes): ")
        if len(key_enc) != 16: 
            print "Enter a 16 bit value!"
    while len(key_mac) != 16: 
        key_mac = raw_input("Enter HMAC Key (16 bytes): ")
        if len(key_mac) != 16: 
            print "Enter a 16 bit value!"
        
    choice = 0
    
    while (choice != 1) and (choice != 2):    
        choice = int(raw_input("Menu: Press - 1 for Encryption, 2 for Decryption: "))
        if (choice != 1) and (choice != 2):
            print "Press either 1 or 2"
        else:
            if choice == 1:
                plain = raw_input("Enter Plain Text: ")
                e = Encrypt()
                print len(plain)
                iv_cipher = e.perform_encryption(key_enc, key_mac, plain)
                print "\n\nCipher Text as Hex String (With IV): "+"".join(x.encode('hex') for x in iv_cipher)+"\n\n"
            else:
                iv_cipher_hex = raw_input("Enter Cipher Text as hex string, starting with an IV (Total length should be greater than 16 bytes): ")
                iv_cipher = iv_cipher_hex.decode('hex')
                d = Decrypt()
                plain = d.perform_decryption(key_enc, key_mac, iv_cipher)
                print "\n\nPlain Text: "+plain+"\n\n"
                print "\n\nPlain Text as Hex String: "+plain+"\n\n"