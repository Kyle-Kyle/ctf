# uncompyle6 version 3.6.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.1 (default, Feb 16 2020, 07:45:27) 
# [GCC 9.2.1 20191109]
# Embedded file name: pybonhash.py
# Compiled at: 2020-03-28 09:11:38
# Size of source mod 2**32: 1017 bytes

import string, sys, hashlib, binascii
from Crypto.Cipher import AES
from flag import key
if not len(key) == 42:
    raise AssertionError
else:
    data = open(sys.argv[1], 'rb').read()
    assert len(data) >= 191
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET

def fibseq(n):
    out = [
     0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out


FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
while i < len(data):
    data1 = data[(FIB[i] % len(data))]
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1

    data2 = data[(FIB[i] % len(data))]
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    i += 1

    tohash = bytes([data1, data2])
    toencrypt = hashlib.md5(tohash).hexdigest()
    thiskey = bytes([key1, key2]) * 16

    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(toencrypt)
    output += binascii.hexlify(enc).decode('ascii')

print(output)
# okay decompiling pybonhash.cpython-36.pyc
