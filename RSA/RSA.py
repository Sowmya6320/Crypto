# Implementation of RSA
from Crypto.Util.number import *

m = "flag{t1me_t0_l3arn_RSA}"

# For creating primes p,q and to calculate modulus
p = getPrime(512)
q = getPrime(512)
n = p*q
phi = (p-1)*(q-1)
e = 65537 # public key parameter e

def egcd(a,b):
	if b == 0:
		return a
	else:
		return egcd(b,a%b)

gcd = egcd(p,q)
def mod_inv(a,b,x1,x2,y1,y2):
	if gcd == 1:	
		if b == 0:
			return x1
		else:
			x = (x1 - ((a/b)*x2))
			y = (y1 - ((a/b)*y2))
			return mod_inv(b,a%b,x2,x,y2,y)
	else:
		print "mod_inv_doesn't_exist"
d = (mod_inv(e,phi,1,0,0,1))%phi


# RSA_Encryption:
m = bytes_to_long(m)
ciphertext = long_to_bytes(pow(m,e,n)).encode("hex")
print ciphertext

# RSA_Decryption
c = bytes_to_long(ciphertext.decode("hex"))
plaintext = pow(c,d,n)
plaintext = long_to_bytes(plaintext)
print plaintext
