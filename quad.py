from sympy import *
x = symbols('x')

print(integrate(x, (x, 1, 2)))  #integrate

k=diff(x**3+x,x)    #diff

print(k)

print(solve(k))