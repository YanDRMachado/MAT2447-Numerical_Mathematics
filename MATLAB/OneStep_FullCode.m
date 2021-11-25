clear 
clc
close all

%métodos one-step

dt = 0.0125;
t = 0:dt:2;

sigma = 10;
beta = 8/3;
rho = 28;

f =@(t,y)([sigma*(y(2)-y(1)); y(1)*(rho-y(3))-y(2); y(1)*y(2)-beta*y(3)]); 

ic = [1 1 1]; %condição inicial do problema 

y_el(:,1) = ic';  %solução no tempo inicial
y_heun(:,1) = ic';
y_elimp(:,1) = ic';

for i = 1:length(t)-1
    y_el(:,i+1) = y_el(:,i) + dt*f(t(i), y_el(:,i)); %método de euler explícito
    tmp = y_heun(:,i) + dt*f(t(i), y_heun(:,i)); 
    y_heun(:,i+1) = y_heun(:,i) + 0.5*dt*[f(t(i+1), y_heun(:,i))+f(t(:,i),tmp)]; %método de heun explícito
    
    y_elimp(:,i+1) = metodo_newton(y_elimp(:,i),dt,f,t(i+1)) %método de euler implícito
end 

[t y_exata] = ode45(f, t, ic); %solução exata da nossa EDO

% for i = 1:size(y_el,1)
% figure
% plot(t, y_el(i,:), t, y_heun(i,:), t, y_exata(:,i), t, y_elimp(i,:), 'LineWidth',2)
% legend('Euler Explícito','Heun','EDO45', 'Euler Implícito')
% set(gca,'Fontsize',12)
% grid on
% end

% figure
% plot3(y_el(1,:), y_el(2,:), y_el(3,:), 'Linewidth', 2) 
% legend('Euler Implícito')
% set(gca,'Fontsize',16)
% 
% figure
% plot3(y_heun(1,:), y_heun(2,:),y_heun(3,:), 'Linewidth', 2)
% legend('Heun')
% set(gca,'Fontsize',16)
% 
% figure
% plot3(y_elimp(1,:), y_elimp(2,:),y_elimp(3,:), 'Linewidth', 2)
% legend('Euler Implícito')
% set(gca,'Fontsize',16)

function [y] = metodo_newton(x, dt, f, t) %método de newton para os métodos implícitos

sigma = 10;
rho = 28;
beta = 8/3;

tol = 1e-6;
F = @(x,y,dt) (x-y-dt*f(t,x));
Jf = @(t, y) ([-sigma, (rho-y(3)), y(2); sigma, -1, y(1); 0, -y(1), -beta]);
% Jf = [-sigma sigma 0; rho-x(3) -1 x(1); x(2) x(1) -beta]
size(Jf)
dJ = @(x,y,dt) (eye(3) - dt*Jf(t,y));

xold = x;
xnew = x;
err = 100;
while err > tol
    delta = dJ(xnew, xold, dt)\F(xnew, xold, dt);
    tmp = xnew;
    xnew = xold - delta;
    err = norm(delta);
    xold = tmp;
end
y = xnew;
end
