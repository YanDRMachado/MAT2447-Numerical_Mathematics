import numpy as np
import matplotlib.pyplot as plt

#defining the general model

def function(x, params):
    
    alpha = params["alpha"]
    beta = params["beta"]
    gamma = params["gamma"]
    delta = params["delta"]
    
    xdot = np.array([alpha*x[0] - beta*x[0]*x[1], delta*x[0]*x[1] - gamma*x[1]])
                     
    return xdot

#rk4 method

def RK4(f, x0, t0, tf, dt):
    
    t = np.arange(t0, tf, dt) #initial time, final time, step
    nt = t.size #number of steps
    
    nx = x0.size
    x = np.zeros((nx, nt)) #matriz com zeros com nx linhas e nt colunas
    
    x[:,0] = x0 #initial values
    
    for k in range(nt - 1):
        k1 = dt*f(t[k], x[:,k])
        k2 = dt*f(t[k] + dt/2, x[:,k] + k1/2)
        k3 = dt*f(t[k] + dt/2, x[:,k] + k2/2)
        k4 = dt*f(t[k] + dt, x[:,k] + k3)
    
        dx = (k1 + 2*k2 + 2*k3 + k4)/6
        
        x[:,k+1] = x[:,k] + dx
    
    return x, t

#defining the problem (the system)

params = {"alpha": 0.25, "beta": 0.01, "gamma": 1, "delta": 0.01}

f = lambda t, x: function(x, params)

#solving the differential equations

x0 = np.array([80, 30])
t0 = 0
tf = 30
dt = 0.01

x, t = RK4(f, x0, t0, tf, dt)

#plotting the results

plt.figure(figsize = (12, 8))
plt.subplot(1, 2, 1)
plt.plot(t, x[0,:], 'r')
plt.plot(t, x[1,:], 'b')
plt.xlabel('Time (t)')
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x[0,:], x[1,:])
plt.grid()
plt.legend()



