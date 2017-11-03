from init import *
from nonlinear_model import *
from eIMTR_control import *
import matplotlib.pyplot as plt

out = f([1,0,0],[1,1])

time = np.arange(0,T,dt)

X = np.zeros((len(time),3))
U = np.zeros((len(time)-1,2))
X[0,:]=x0

for i in range(0,len(time)-1):
    u = eIMTR_control(time[i])
#    xdot = f(X[i,:],u)
#    X[i+1,:] = X[i,:] + dt*xdot
    U[i,:] = u;
    print(i,'out of',len(time),': r =',X[i,0])
print('len of time =',len(time[:-1]),'and len(U) =',len(U))
plt.plot(time[:-1],U[:,0]/3600)
plt.show()
    
