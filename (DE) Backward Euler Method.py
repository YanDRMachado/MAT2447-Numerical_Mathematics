'''python 3.7.9'''
# por se tratar de um problema implícito (dependência de u_n+1 para o cálculo de u_n+1)  
# podemos utilizar aproximações do método de newton a cada passo

import numpy as np
import matplotlib.pyplot as plt

def eulerforward(f, y0, n, h): #resolve u' = f(y, t), com u(0)=u0 e n passos até h
    t = np.zeros(n+1)  
    y = np.zeros(n+1)
    y[0] = y0
    t[0] = 0
    dt = h/n
    for i in range(n):
        t[i + 1] = t[i] + dt
        y[i + 1] = y[i] + dt*f(y[i+1], t[i+1]) #definição do backward euler method
    return y, t


def f(y, t):  #ex: u'=2*u, função exp(2*x)
    return -4*y + t**2


# y, t = eulerforward(f, y0=1, h=4, n=1000)
# plt.plot(t, y, linestyle="dashed")'

plt.figure(figsize = (12, 8))
for n in [2, 5, 10, 100]: #para ver a solução se aproximando da função com aumento do número de passos
    y, t = eulerforward(f, y0=1, h=1, n=n)
    plt.plot(t, y, linestyle="dashed")

# func = np.linspace(-4, 4, 1000)
# plt.figure(figsize = (12,8)) 
# plt.plot(-2*t**2,'k') #plotar a função correta para comparar 
# # plot.legend()
# plt.show()

plt.plot(t, 4*y**2,'k') #plota
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.show()

print('Erro em cada ponto: ', f(y,t) - y)
print(y, t)