from Crypto.Util.number import *
from sage.all import *

p = 6971096459 * 261841354058939 * 9293011496905768559 * 336286207038529046808347 * 21472883178031195225853317139
g = 2
h = 41265478705979402454324352217321371405801956976004231887598587967923553448391717998290661984177

# p factors:   6971096459 * 261841354058939 * 9293011496905768559 * 336286207038529046808347 * 21472883178031195225853317139

pfact = [6971096459 , 261841354058939 , 9293011496905768559 , 336286207038529046808347 , 21472883178031195225853317139]

def Log(pfact,g,h):
	a = []
	for i in pfact:
		F = IntegerModRing(i)
		h1 = h%i
		print h1
		b = discrete_log(F(h1),F(g))
		a.append(b)
	print a
	return a

def Crt(a,pfact,g,h,p):
	phi = []
	for i in pfact:
		phi.append(i - 1)
	print phi,a
	x = crt(a,phi)
	print pow(g,x,p) == h
	return x

a = Log(pfact,g,h)
x = Crt(a,pfact,g,h,p)
print x 
		
