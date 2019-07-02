from Crypto.Util.number import *
from sage.all import *
N = 97
E = EllipticCurve(GF(N),[2,3])
P = E(3,6)
Q = E(80,87)

#For pollard rho order wrt g must be prime. 
#Q = x*P
def partition(h,a,b,P,Q,n,N):
	k = int(h[0])%3
	if k == 0:
		h = (h + P)
		a = (a + 1)%n

	if k == 1:
		h = (h + Q)
		b = (b + 1)%n

	if k == 2:
		h = (2*h)
		a = (2*a)%n
		b = (2*b)%n

	return h,a,b

def verify(P,Q,N,x):
	return P*x == Q

def pollard_rho(P,Q,N):
	h0 = P + Q 
	s = h0
	t = h0
	a=1
	b=1
	a1=1
	b1=1
	n = P.order()
	for i in xrange(1,n):
		s,a,b = partition(s,a,b,P,Q,n,N)
		t,a1,b1 = partition(t,a1,b1,P,Q,n,N)
		t,a1,b1 = partition(t,a1,b1,P,Q,n,N)
		if s == t:
			break
	nom = a - a1
	denom = b1 - b   
	x = (inverse(denom,n)*nom)%n

	if verify(P,Q,N,x):
		return x
	return x + n

x = pollard_rho(P,Q,N)
print P*x == Q
print P
print P*x , Q
print x
