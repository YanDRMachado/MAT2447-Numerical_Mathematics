clear 
clc
close all

%runge-kutta 4a ordem

f = @LotkaVolterraModel;
x0 = [80; 30];

t0 = 0;
tf = 50;
dt = 0.01;

[x, t] = RungeKutta45(f, x0, t0, tf, dt);

figure;

plot(t,x)
legend('t','x')
xlabel('Time (t)')
grid on;

figure
plot(x(1,:), x(2,:))


function xdot = LotkaVolterraModel(t,x)
    
    alpha = 0.25;
    beta = 0.01;
    gamma = 1;
    delta = 0.01;
    
    xdot = [alpha*x(1) - beta*x(1)*x(2)
           delta*x(1)*x(2) - gamma*x(2)];    

end

function [x,t] = RungeKutta45(f, x0, t0, tf, dt)

    t = t0:dt:tf;
    nt = numel(t)
    nx = numel(x0);

    x = nan(nx, nt); 
    
    x(:,1) = x0;
    
    for k = 1:nt-1
        
        k1 = dt*f(t(k), x(:,k))
        k2 = dt*f(t(k) + dt/2, x(:,k) + k1/2)
        k3 = dt*f(t(k) + dt/2, x(:,k) + k2/2)
        k4 = dt*f(t(k) + dt, x(:,k) + k3)
        
        dx = (k1 + 2*k2 + 2*k3 + k4)/6
        
        x(:,k+1) = x(:,k) + dx;
    end
     
end


