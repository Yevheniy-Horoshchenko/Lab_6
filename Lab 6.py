import math
from scipy import optimize
x0=-0.65
y0=0.15
def f1(y):
    return -0.8 + math.sin(y)/2
def f2(x):
    return -0.8 + math.cos(x+0.5)
def iter (x,y,e):
    xn=x
    yn=y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn)>=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n += 1
    print ('x1= ',xn,'\ny1',yn,'\nThe amount of iteration = ',n)
    iter (x0,y0,0.0001)
    def f(x):
        return math.cos(x[0]+0.5)+x[1]-0.8,math.sin(x[1])-2*x[0]-1.6
    s = optimize.root(f,[0,0],method = 'hybr')
    print (s.x)