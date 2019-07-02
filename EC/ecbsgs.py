from sage.all import *
from math import sqrt,ceil
from Crypto.Util.number import *

def bsgs(enc,g):            
	m = int(ceil(sqrt(g.order())))
	gin = m*g
	values = []
	for j in range(m):
		values.append(j*g) 
	for i in range(0,m):
		k = (enc - (i*gin))
		if k in values:
			return (i*m + values.index(k))

'''
E = EllipticCurve(GF(17),[2,2])
p = E(5,1)
print bsgs(17*p,p), bsgs(19*p,p)*p 
'''

N = 157
E = EllipticCurve(GF(N),[77,28])
P = E(57,41)
Q = E(57,41)
ord_ = P.order()
print bsgs(Q,P)
