#!/usr/bin/python

'''
@author: Rahil Arora
@contact: rahil@jhu.edu
'''

import itertools
import hashlib
import time
import json

generate_file = raw_input("Do you want to generate a JSON file? (y/n): ") 


'''
This part takes care of computing all the passwords in Special4
'''

password_hashes = {}
passwords4_all = [''.join(i) for i in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz", repeat=4)]
passwords4_not_special4 = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4)]
passwords4_special4 = list(set(passwords4_all) - set(passwords4_not_special4))


passwords3_all = [''.join(i) for i in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz", repeat=3)]
passwords3_not_special4 = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3)]
passwords3_special4 = list(set(passwords3_all) - set(passwords3_not_special4))


passwords2_all = [''.join(i) for i in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz", repeat=2)]
passwords2_not_special4 = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=2)]
passwords2_special4 = list(set(passwords2_all) - set(passwords2_not_special4))


passwords1_all = [''.join(i) for i in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz", repeat=1)]
passwords1_not_special4 = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=1)]
passwords1_special4 = list(set(passwords1_all) - set(passwords1_not_special4))

passwords_special4 = passwords4_special4 + passwords3_special4 + passwords2_special4 + passwords1_special4


'''
This part takes care of generating the SHA1 hashes
'''

print "\n\nPlease wait while the hashes are being generated...\n\n"
start_time = time.time()
for password in passwords_special4:
    hash = hashlib.sha1(password).hexdigest()
    password_hashes[password] = hash 
end_time = time.time()
print "All possible passwords possible in special4: ", len(passwords_special4)
print "Total time(in sec): ", end_time - start_time
print "\n\n"


'''
This part takes care of generating a JSON file
'''

if generate_file in ['y','Y','yes', 'Yes', 'YES']:
    print("Generating JSON file...\n\n")
    with open('password_hashes.json', 'w') as f:
        json.dump(password_hashes, f)
