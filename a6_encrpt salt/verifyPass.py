import hashlib
import sys
import os
import binascii

try:
    hash_name = sys.argv[1]
except IndexError:
    print('Specify the hash name as the first argument.')
else:
    try:
        username = sys.argv[2] 
        passwd = sys.argv[3]
        password = bytes(passwd,'UTF-8')      
    except IndexError:    
        print('using default password: password')
        password = b'password'

    #password = bytes(passwd,'UTF-8')
    salT_file = open(username+"_salt.key")
    chef_salt = salT_file.read()
    print("Salt\n"+chef_salt)

    dk = hashlib.pbkdf2_hmac(hash_name, password, bytes(chef_salt,'UTF-8'), 100000,128)

    hashk = binascii.hexlify(dk)

    new_hash = hashk.decode('utf-8')
    hash_file = open(username+"_hash.hash")
    old_hash  = hash_file.read()

    print("hash\n"+old_hash)
    if new_hash == old_hash:
    	print("The user "+username+" has used valid password")
    else:
    	print("Incorrect username or password")

