from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
phi = (p-1)*(q-1)
m = "flag{Ch33rs_f0r_1mpl3m3nt1ng_th3_4tt4ck!}"

def egcd(a,b):
	if b == 0:
		return a
	else:
		return egcd(b,a%b)

def mod_inv(a,b,x1,x2,y1,y2):
	gcd = egcd(p,q)
	if gcd == 1:	
		if b == 0:
			return x1
		else:
			x = (x1 - ((a/b)*x2))
			y = (y1 - ((a/b)*y2))
			return mod_inv(b,a%b,x2,x,y2,y)
	else:
		print "mod_inv_doesn't_exist"

# Exploit
m = bytes_to_long(m)
d = (mod_inv(e,phi,1,0,0,1))%phi
r = 13907
c = pow(m,e,n)
c1 = c * pow(r,e,n)
d1 = pow(c1,d,n)
pt = d1/r
print long_to_bytes(pt)
print m == pt
