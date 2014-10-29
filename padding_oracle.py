'''
@author: Rahil Arora
@contact: rahil@jhu.edu
'''

import StringIO, sys
import urllib, urllib2, cookielib

from lxml import html

cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)

conn_request = urllib2.Request("http://107.20.120.208/main_login.php")
conn_response = urllib2.urlopen(conn_request)

def parse_url():
    doc = conn_response.read()
    f = StringIO.StringIO(doc)
    tree = html.parse(f)
    captchas = tree.xpath('//input[@name="captchaID"]/@value')
    captcha_id = captchas[0]
    ivs = tree.xpath('//input[@name="iv"]/@value')
    iv = ivs[0]
    return [iv, captcha_id]
    
def strxor(a, b):
        return "".join(chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b))

def request_image(captcha):
    guess_encoded = ((captcha.encode('base64')).replace('+', '-')).replace('/', '_')
    img_url = "http://107.20.120.208/securimage/securimage_show.php?captchaID2="+guess_encoded
    conn_request = urllib2.Request(img_url)
    conn_response = urllib2.urlopen(conn_request)
    html = conn_response.read()
    return html
    

print "\n\nPractical Crypto - A1 - Problem 2 \nSolution by Rahil Arora (JHID: rarora7)\n\nHacking in Progress...Trying to break CAPTCHA at 107.20.120.208\n\n"

progress = 1
iv_captcha_id = parse_url()
iv = iv_captcha_id[0]
captcha_id = iv_captcha_id[1]
iv_decoded = iv.decode('base64')
captcha_id_decoded = captcha_id.decode('base64')
temp_block = chr(0) * 32
current_block = captcha_id_decoded[32:]
previous_block = captcha_id_decoded[16:32]
guess = temp_block + current_block
plaintext = ['']*48


#Cracking firt block!

'''
for j in range(16):
    for i in range(256):
        temp_block_list = list(temp_block)
        temp_block_list[31-j] = chr(i)
        temp_block = ''.join(temp_block_list)
        guess = temp_block + current_block
        html = request_image(guess)
        if html == "Invalid MAC!" and j == 0:
            temp_block_list = list(temp_block)
            temp_block_list[30] = chr(1)
            temp_block = ''.join(temp_block_list)
            guess = temp_block + current_block
            html2 = request_image(guess)
            if html2 == 'Invalid MAC!':
                plaintext[47-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
        elif html == "Invalid MAC!" and j > 0:
            plaintext[47-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
    temp_block = chr(0) * 32
    for m in range(j+1):
        xo = ord(previous_block[15-m]) ^ plaintext[47-m] ^ (j+2)
        temp_block_list = list(temp_block)
        temp_block_list[31-m] = chr(xo)
        temp_block = ''.join(temp_block_list)
    sys.stdout.write("\r" + "."*progress)
    progress = progress + 1
    sys.stdout.flush()
         
print "\n\n\nWork In Progress...\n\n"
progress = 1

# Cracking second block!
 
temp_block = chr(0) * 32
current_block = captcha_id_decoded[16:32]
previous_block = captcha_id_decoded[0:16]
guess = temp_block + current_block
for j in range(16):
    for i in range(256):
        temp_block_list = list(temp_block)
        temp_block_list[31-j] = chr(i)
        temp_block = ''.join(temp_block_list)
        guess = temp_block + current_block
        html = request_image(guess)
        if html == "Invalid MAC!" and j == 0:
            temp_block_list = list(temp_block)
            temp_block_list[30] = chr(1)
            temp_block = ''.join(temp_block_list)
            guess = temp_block + current_block
            html2 = request_image(guess)
            if html2 == 'Invalid MAC!':
                plaintext[31-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
        elif html == "Invalid MAC!" and j > 0:
            plaintext[31-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
    temp_block = chr(0) * 32
    for m in range(j+1):
        xo = ord(previous_block[15-m]) ^ plaintext[31-m] ^ (j+2)
        temp_block_list = list(temp_block)
        temp_block_list[31-m] = chr(xo)
        temp_block = ''.join(temp_block_list)
    sys.stdout.write("\r" + "."*progress)
    progress = progress + 1
    sys.stdout.flush()
        
print "\n\nAlmost there...\n\n"
progress = 1

'''

# Cracking third block

temp_block = chr(0) * 32
current_block = captcha_id_decoded[0:16]
previous_block = iv_decoded
guess = temp_block + current_block
for j in range(16):
    for i in range(256):
        temp_block_list = list(temp_block)
        temp_block_list[31-j] = chr(i)
        temp_block = ''.join(temp_block_list)
        guess = temp_block + current_block
        html = request_image(guess)
        if html == "Invalid MAC!" and j == 0:
            temp_block_list = list(temp_block)
            temp_block_list[30] = chr(1)
            temp_block = ''.join(temp_block_list)
            guess = temp_block + current_block
            html2 = request_image(guess)
            if html2 == 'Invalid MAC!':
                plaintext[15-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
        elif html == "Invalid MAC!" and j > 0:
            plaintext[15-j] = ord(previous_block[15-j]) ^ i ^ (j+1)
    temp_block = chr(0) * 32
    for m in range(j+1):
        xo = ord(previous_block[15-m]) ^ plaintext[15-m] ^ (j+2)
        temp_block_list = list(temp_block)
        temp_block_list[31-m] = chr(xo)
        temp_block = ''.join(temp_block_list)
    sys.stdout.write("\r" + "."*progress)
    progress = progress + 1
    sys.stdout.flush()
        
print "\n\n\nDone!\n\n"

pt_list = plaintext[:6]
pt = "".join(chr(x) for x in pt_list)
final_captcha = pt[:6]

print "CAPTCHA: " + final_captcha + "\n\n"

login_url = 'http://107.20.120.208/check_login.php'
params = urllib.urlencode({'login_captcha':final_captcha, 'captchaID':captcha_id, 'iv':iv})
req = urllib2.Request(login_url, params)
rsp = urllib2.urlopen(req)
data = rsp.read()
print data