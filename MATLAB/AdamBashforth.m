clear 
clc
close all

 n = 100 %número de passos
 x(1)=0 %valor inicial de x
 y(1)=0.5 %valor inicial de y
 x(n)=10 %y final
 h=(x(n)-x(1))/(n-1);
 f(1)=EDO(x(1),y(1));

%  RK4 para comparação e cálculo de erro

 for i=1:n-1
     
   K1=h*EDO(x(i),y(i));
   K2=h*EDO(x(i)+h/2,y(i)+K1/2);
   K3=h*EDO(x(i)+h/2,y(i)+K2/2);
   K4=h*EDO(x(i)+h,y(i)+K3);

 y(i+1)=y(i)+(1/6)*(K1+2*K2+2*K3+K4);
 x(i+1)=x(i)+h;
   f(i+1)=EDO(x(i+1),y(i+1));   
   
 end
   
figure
plot (x,y)
title('RK4')
hold on
    
% AB

 for i=4:n-1

 y(i+1)=y(i)+(h/24)*(55*f(i) - 59*f(i-1) + 37*f(i-2) - 9*f(i-3));
    x(i+1)=x(i)+h;
  f(i+1)=EDO(x(i+1),y(i+1));
     
 end

figure
plot (x,y,'r')
title('Adam Bashforth')
hold off

function F=EDO(x,y)
 
F= -y*log(y);

end