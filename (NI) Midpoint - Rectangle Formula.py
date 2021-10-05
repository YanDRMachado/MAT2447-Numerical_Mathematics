'''python 3.7.9'''

import numpy as np
import scipy.integrate as integrate

f = lambda x: x*np.exp(-1*x)*np.cos(2*x) #função a ser integrada
a = 0 #início do intervalo de integração
b = np.pi*2 #final do intervalo de integração
N = 10 #número de subintervalos, ^ número ^ precisão
x = np.linspace(a, b, N+1)
y = f(x)

#função da Fórmula Retangular (Midpoint)

def midpoint(f, a, b, N):
    H = float(b-a)/N
    result = 0
    for i in range(N):
        result += f((a + H/2) + i*H)
    result *= H
    return result


print("Midpoint/Rectangular")
Area = midpoint(f, a, b, N)
print("Área = ", Area)

Int, E = integrate.quad(f, a, b) #"general purpose integration command"
print('Erro = ', np.abs(Int - Area))

