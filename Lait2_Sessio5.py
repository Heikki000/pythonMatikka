'''
Tehtäviä
3. Laske funktion 𝑓(𝑥)=𝑒**(−𝑥**2)
derivaatan numeerinen likiarvo kolmipistekaavalla pisteessä x = 1.5. Käytä askelpituutta dx = 0.001.
4. Laske funktion 𝑔(𝑥)=(𝑥−1) / (𝑥+1)
derivaatan numeerinen likiarvo kolmipistekaavalla pisteessä x = 0.3. Käytä askelpituutta dx = 0.001.

'''
#1. Laske sympyllä esimerkin 2𝑥**2 − 3  derivaatta.
from sympy import symbols, diff, exp, sin
x = symbols('x')
f = 2 * x**2 - 3
derivative = diff(f, x)
print("Funktion derivaatta:", derivative)

#2. Laske funktion f (x)=sin x derivaatta numeerinen likiarvo kaksi- ja kolmepistekaavalla
#käyttäen askelpituutta Δ x=0,001.
import numpy as np

def f(x):
    return np.sin(x)

def derivative_two_point(x, dx):
    return (f(x + dx) - f(x)) / dx

def derivative_three_point(x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)

derivative_two = derivative_two_point(2,0.001)
derivative_three = derivative_three_point(x, dx)
virhe = np.abs(derivative_two - 4)

print("Kahdenpisteen kaavalla derivaatan likiarvo:", derivative_two)
print("Virhe: ", )


