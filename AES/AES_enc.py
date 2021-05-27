from Crypto.Cipher import AES
from Crypto.Util.number import *
import os
from Crypto.Util import Counter


key = os.urandom(16)
iv = os.urandom(16)
BLOCKSIZE = 16

def pad(s):
	pad = s + (BLOCKSIZE - (len(s) % BLOCKSIZE))*(chr(BLOCKSIZE - (len(s) % BLOCKSIZE)))
	return pad


def ecb_encryption(plaintext):
	plaintext = pad(plaintext)
	print len(plaintext) % BLOCKSIZE == 0
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext = cipher.encrypt(plaintext)
	return ciphertext.encode("hex")


def cbc_encryption(plaintext):
	plaintext = pad(plaintext)
	print len(plaintext) % BLOCKSIZE == 0
	cipher = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = cipher.encrypt(plaintext)
	return ciphertext.encode("hex")


def ctr_encryption(plaintext):
	ctr=Counter.new(128)
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	ciphertext = cipher.encrypt(plaintext)
	return ciphertext.encode("hex")

plaintext = "Pycrypto implementation of AES modes of encryption"
print ecb_encryption(plaintext)
print cbc_encryption(plaintext)
print ctr_encryption(plaintext)
