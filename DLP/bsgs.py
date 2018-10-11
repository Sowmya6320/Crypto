# Function to perform Baby Step Giant Step Attack. This function only works for small integers
# enc = pow(g,msg,p)

def bsgs(enc,g,p):
	m = int(ceil(sqrt(p)))
	g_inv = gmpy.invert(g,p)	
	values = []
	for j in range(m):
		values.append(pow(g,j,p))
	for i in range(1,m):
		k = (enc*(pow(g_inv,i*m,p)))%p
		if k in values:
			return i*m + values.index(k)
