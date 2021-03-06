'''python 3.7.9'''

'''método de Newton para uma única equação'''

import numpy as np
import matplotlib.pyplot as plt

#polinômio quadrático

def f(x):
    return x**3 - 10*x**2 + 29*x - 20

#derivada do polinômio escolhido

def df(x):
    return 3*x**2 - 20*x + 29

max_it = 20 #número máximo de iterações (evitar loop eterno)
x = -1 #chute inicial
res = abs(f(x)) #resíduo

i = 0
while (res > 1e-8):
    print(i, x, f(x))
    x = x - f(x) / df(x)
    res = abs(f(x)) #atualizar o valor do resíduo
    i += 1 #atualizar o valor de i

    if (i > max_it):
        print(i, x, f(x))
        print("O método não convergiu")
        break
    
print(i, x, f(x))

#plot

xplt = np.linspace(-4, 4, 100) 
plt.figure(figsize = (12, 8))
plt.plot([-4, 4], [0,0],'k--') #reta horizontal correspondente ao eixo x
plt.plot(xplt, f(xplt), 'b-') #função polinomial escolhida
plt.plot(x, f(x), 'go') #ponto encontrado através do método
plt.xlabel('x')
plt.ylabel('y')
plt.show()


'''para um sistema de equações multivariáveis, versão final'''

#definindo o sistema de equações que queremos resolver

def f(xyz):
    x,y,z=xyz
    return [x**2 + y**2 + z**2 - 25,
            x*y + y*z + z*x - 5,
            x + y - 3]

#definindo a Matriz Jacobiana

def jacobiano(xyz): #ou (import autograd.numpy as np, from autograd import grad, jacobian), jacobian(f)
    x,y,z=xyz
    return [[2*x, 2*y, 2*z],
            [y, z, x],
            [1, 1, 0]]

#definindo a função com o método de Newton

def newton(fun, x_inicial, jaco):
    max_it = 100 #número máximo de iterações (evitar loop eterno)
    res = 1e-8 #resíduo
    
    x_final = x_inicial
    for i in range(max_it):
        J = np.array(jaco(x_final))
        F = np.array(fun(x_final))
        delta = np.linalg.solve(J,-F)
        x_final = x_final + delta
        
        if np.linalg.norm(delta) < res:
            print('Converge para i ''= ', i)
            break
    else:
            print('O método não convergiu')  
            
    return x_final
    
chute_inicial = [1,2,2] #chute inicial

resp = newton(f, chute_inicial, jacobiano)
print(resp)
