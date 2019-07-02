from sage.all import *
from Crypto.Util.number import *

def hensel_lift_curves(f,p,point):
	A, B = map(long, (E.a4(), E.a6()))
	x, y = map(long, point.xy())
	fr = (y**2 - (x**3 + A*x + B))
	return x , (y - (Integer((fr)*inverse_mod(2*y,p))))%p**2

def smarts_attack(f,p,P,Q):
	x1, y1 = hensel_lift_curves(f,p,P)
	x2, y2 = hensel_lift_curves(f,p,Q)

	A = (((y2**2 - y1**2) - (x2**3 - x1**3))*inverse_mod(x2-x1,p**2))%p**2
	B = (y1**2 - x1**3 - A*x1)%p**2
	mod = p**2
	EC = EllipticCurve(IntegerModRing(mod), [A,B])

	P1 = EC(x1,y1)
	Q1 = EC(x2,y2)

	P_1 = (p-1)*P1
	Q_1 = (p-1)*Q1

	mx,my = map(long, P_1.xy())
	nx,ny = map(long, Q_1.xy())

	x1_ = (mx - x1) / p
	x2_ = (my - y1) / p
	y1_ = (nx - x2)
	y2_ = (ny - y2)
	 
	m = y1_ * inverse_mod(x1_, p) * x2_ * inverse_mod(y2_, p)
	m %= p	 
	return m

p = 853
E = EllipticCurve(GF(p), [108,4])
P = E(0,2)
Q = E(563,755)
m = smarts_attack(E,p,P,Q)
