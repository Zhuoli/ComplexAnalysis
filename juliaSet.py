from math import sqrt
C = 1
R = (1+sqrt(1+4*abs(C)))/2
a=-3 
b=3
c=-3
d=3
maxiter = 100

def f(z):
    return z**2+C

p=1j
print("R is: " + str(R))
for i in range(maxiter):
    p = f(p)
    print(p)

