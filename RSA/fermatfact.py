from Crypto.Util.number import *
from math import sqrt,ceil
import gmpy

m = "flag{f3rmat_f4ct0ris4ti0n_1snt_e4sy_1s_1t?}"
n = 16597712262800095098226130512282927179497011173406539443409876664765634654792363184411825406484837021057998483611151825837103388795480529002121502546121948928066281359031028270878297218661409934035886546020930964028780335737680348596910306513206117504108058925329858396067856573163592825383960058578681644875980180546847557812966223271765120162910255137784213094212309609759257353674875979882725784871783757837297703281196379092511265281287845023919390729682379344606965288462358145824117145872183931465422694130609005144944508184194344888497580577863328136806345023037939204996365581479722451260520977982655414777159
e = 65537

# RSA_Encryption:
def encrypt(m):
	m = bytes_to_long(m)
	ciphertext = long_to_bytes(pow(m,e,n)).encode("hex")
	return ciphertext

a = (gmpy.mpz(n)).root(2)
a1 = a[0] + 1
if a1**2 < n:
	print "error"

def ff(n,a):
	if n%2 == 1:
		b2 = a**2 - n
		b2 = gmpy.mpz(b2)
		z = b2.root(2)		
		if (z[0])**2 == b2:
			return z[0] , a
		else:
			return ff(n,a+1)
	else:
		print "not_possible"

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

#RSA_Decryption
def decrypt(c):
	c = bytes_to_long(c.decode("hex"))
	plaintext = pow(c,d,n)
	plaintext = long_to_bytes(plaintext)
	return plaintext
c = encrypt(m)

a = (gmpy.mpz(n)).root(2)
a1 = a[0] + 1
if a1**2 < n:
	print "error"
b , a = ff(n,a1)
p1 = int(a + b)
q1 = int(a - b)
if n == p1*q1:
	print "Factorised"
phi1 = (p1-1)*(q1-1)
d = mulinv(e,phi1)
print decrypt(c)
