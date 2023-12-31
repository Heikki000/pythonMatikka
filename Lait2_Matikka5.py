#Laitteisto2 / Matikka 5
#1. Laske sympyllä esimerkin 2𝑥**2 − 3  derivaatta.
from sympy import symbols, diff
x = symbols('x')
derivative = diff(2 * x**2 - 3, x)

print("Funktion 2 * x**2 - 3 derivaatta on", derivative, ".")

#2. Laske funktion f (x)=sin x derivaatta numeerinen likiarvo kaksi- ja kolmepistekaavalla
#käyttäen askelpituutta Δ x=0,001.
import numpy as np

def f(x):
    return np.sin(x)
dx = 0.001
x = 1

derivaatta_2_1 = (f(x + dx) - f(x))/dx
virhe_2 = np.abs(derivaatta_2_1 - np.cos(x))
print('Derivaatta(2):', derivaatta_2_1, '     Virhe:', virhe_2)

derivaatta_2_2 = (f(x + dx) - f(x - dx)) / (2 * dx)
virhe_3 = np.abs(derivaatta_2_2 - np.cos(x))
print('Derivaatta(3):', derivaatta_2_2, '     Virhe:', virhe_3)

#3. Laske funktion 𝑓(𝑥)=𝑒**(−𝑥**2) derivaatan numeerinen likiarvo
# kolmipistekaavalla pisteessä x = 1.5. Käytä askelpituutta dx = 0.001.

def f(x):
    return np.e ** (-1*x ** 2)
x = 1.5
derivaatta_3_1 = (f(x + dx) - f(x - dx)) / (2 * dx)
print('Derivaatta(3_1):', derivaatta_3_1, '.')

# 4. Laske funktion 𝑔(𝑥)=(𝑥−1) / (𝑥+1) derivaatan numeerinen likiarvo
# kolmipistekaavalla pisteessä x = 0.3. Käytä askelpituutta dx = 0.001.

def g(x):
    return (1*x - 1) / (1*x + 1)
x = 0.3
derivaatta_4 = (g(x + dx) - g(x - dx)) / (2 * dx)
print('Derivaatta_4:', derivaatta_4, '.')





