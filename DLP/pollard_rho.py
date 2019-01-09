from Crypto.Util.number import *
#N = 383
#g = 2
#y = 228
g,y,N = (2,4178319614L,6971096459)

#For pollard rho order wrt g must be prime. 
#y = pow(g,x,N)
def partition(h,a,b,g,y,n,N):
    k = h%3
    if k == 0:
        h = (g*h)%N
        a = (a + 1)%n

    if k == 1:
        h = (y*h)%N
        b = (b + 1)%n

    if k == 2:
        h = (h*h)%N
        a = (2*a)%n
        b = (2*b)%n

    return h,a,b

def verify(g,y,N,x):
    return pow(g, x, N) == y


def pollard_rho(g,y,N):
    h0 = g*y
    s = h0
    t = h0
    a=1
    b=1
    a1=1
    b1=1
    n = (N-1)/2
    for i in xrange(1,n):
        s,a,b = partition(s,a,b,g,y,n,N)
        t,a1,b1 = partition(t,a1,b1,g,y,n,N)
        t,a1,b1 = partition(t,a1,b1,g,y,n,N)
        if s == t:
            break
    nom = a - a1
    denom = b1 - b   
    x = (inverse(denom,n)*nom)%n

    if verify(g,y,N,x):
        return x
    return x + n

x = pollard_rho(g,y,N)
print pow(g,x,N) == y
print x
