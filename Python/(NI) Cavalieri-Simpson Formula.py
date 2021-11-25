'''python 3.7.9'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

#f é a função, a < intervalo < b, N é o número de subintervalos

f = lambda x: np.sign(x - np.pi) #função a ser integrada
a = -3 #início do intervalo de integração
b = 5 #final do intervalo de integração)
N = 100 #número de subintervalos, ^ número ^ precisão (exceto para funções modulares)
x = np.linspace(a, b, N+1)
y = f(x)

#função da fórmula de Cavalieri-Simpson

def cavalierisimpson(f, a, b, N):
    if N % 2 == 1: #caso o resto da divisão N/2 = 1 -> N é impar e deve ser modificado
        raise ValueError('O input N ser par.')
    H = (b-a)/N
    Integral = H/6 * 2 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return Integral

print("Cavalieri-Simpson")
Area = cavalierisimpson(f, a, b, N)
print("Área = ", Area)

Int, E = integrate.quad(f, a, b) #"general purpose integration command"
print('Erro = ', np.abs(Int - Area))


#X e Y são os valores para o plot de y=f(x)

X = np.linspace(a, b, 100)
Y = f(X)
plt.plot(X,Y)

for i in range(N):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, f(x[i]), f(x[i+1]), 0]
    plt.fill(xs, ys, 'b', edgecolor='r', alpha=0.2)

plt.title('Fórmula de Cavalieri-Simpson, N={}'.format(N))
plt.show()

