'''python 3.7.9'''

import numpy as np
import matplotlib.pyplot as plt

def eulerforward(f, u0, h, n): #resolve u' = f(u, t), com u(0)=u0 e n passos até h
    t = np.zeros(n+1)  #cria um array de zeros
    u = np.zeros(n+1)
    u[0] = u0
    t[0] = 0
    dt = h/n
    for k in range(n):
        t[k + 1] = t[k] + dt
        u[k + 1] = u[k] + dt*f(u[k], t[k]) #definição do forward euler method
    return u, t


def f(u, t):  #u'=2*u, função exp(2*x)
    return 2*u


# u, t = eulerforward(f, u0=1, h=4, n=1000)
# plt.plot(t, u, linestyle="dashed")'

for n in [5, 10, 20, 50, 100]: #para ver a solução se aproximando da função com aumento do número de passos
    u, t = eulerforward(f, u0=1, h=4, n=n)
    plt.plot(t, u, linestyle="dashed")

func = np.linspace(0, 4, 1000) 
plt.plot(func, np.exp(2*func)) #plotar a função correta para comparar 
# plot.legend()
plt.show()

