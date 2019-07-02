def ecbsgs(enc,g):            
	m = int(ceil(sqrt(g.order())))
	gin = m*g
	values = []
	for j in range(m):
		values.append(j*g) 
	for i in range(0,m):
		k = (enc - (i*gin))
		if k in values:
			return (i*m + values.index(k))

def ecpohlig(alph,beta,p):
	factors = list(factor(p))
	x = []
	qe = []
	for q,e in factors:
		qe.append(q**e) 
		alph0 = alph*(p//(q**e)) 
		beta_i = beta*(p//(q**e))
		beta0 = beta_i
		tmpalph = alph0 * q**(e-1)
		Xi = 0
		for i in range(e):
			tmpbeta = beta0 * q**(e-(i+1))
			x_i = ecbsgs(tmpbeta,tmpalph)
			Xi = Xi + x_i*(q**i)
			beta0 = beta_i - Xi*(alph0)
		x.append(Xi)
	X = crt(x,qe)
	print X , X*alph == beta
	return X

N = 157
E = EllipticCurve(GF(N),[77,28])
P = E(20982, 1348)
Q = 3343*P
ord_ = P.order()
print ecpohlig(P,Q,ord_)
