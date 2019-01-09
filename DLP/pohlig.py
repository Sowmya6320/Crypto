from Crypto.Util.number import *
from sage.all import *

def pohlig(alph,beta,p):
	factors = list(factor(p-1))
	x = []
	qe = []
	for q,e in factors:
		beta_i = beta
		qe.append(q**e)
		alph0 = pow(alph,(p-1)//q,p)
		F = IntegerModRing(p)
		Xi = 0
		for i in range(e):
			tmpbeta = pow(beta_i,(p-1)//q**(i+1),p)
			x_i = discrete_log(F(tmpbeta),F(alph0))
			print "*****x_i****:" + str(x_i)
			beta_i = (beta_i*pow(inverse(alph,p),x_i*(q**(i)),p))%p
			Xi = Xi + x_i*(q**i)
		x.append(Xi)
	X = crt(x,qe)
	print X , pow(alph,X,p) == beta

alph = 3
beta = 237
p = 257
pohlig(alph,beta,p)
