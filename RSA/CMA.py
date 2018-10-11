#Common_Modulus_Attack
#Situation: Alice, Bob, Chris and Eve are connected over a public network. Let their public key encryption exponents be (eA,eB,eC) and have a common modulus 'n'.Also eB != eC and gcd(eB,eC) = 1. Alice sends a secret message to Bob and Chris, so will Eve be able to decipher it?

from Crypto.Util.number import *

msg = "flag{B3war3!!_Eve_1s_Spy1ng_U}"

p = getPrime(512)
q = getPrime(512)
#p = 191
#q = 307
n = p*q
e = [44701,65537]

def egcd(a,b):
	if b == 0:
		return a
	else:
		return egcd(b,a%b)

def mod_inv(a,b,x1,x2,y1,y2):
  gcd = egcd(a,b)
	if gcd == 1:	
		if b == 0:
			return x1 , y1
		else:
			x = (x1 - ((a/b)*x2))
			y = (y1 - ((a/b)*y2))
			return mod_inv(b,a%b,x2,x,y2,y)
	else:
		print "mod_inv_doesn't_exist"

# RSA_Encryption:
def rsa_encrypt(m,e,n):
	m = bytes_to_long(m)
	ciphertext = long_to_bytes(pow(m,e,n)).encode("hex")
	return ciphertext

# Exploit:
c1 = bytes_to_long((rsa_encrypt(msg,e[1],n)).decode("hex"))
c2 = bytes_to_long((rsa_encrypt(msg,e[0],n)).decode("hex"))
a,b = mod_inv(e[1],e[0],1,0,0,1)
if a<0:
	i = mod_inv(c1,n,1,0,0,1)	
if e[1]*a + e[0]*b == 1:
	plaintxt = (pow(i[0],-a,n)*pow(c2,b,n))%n
	print long_to_bytes(plaintxt) 



