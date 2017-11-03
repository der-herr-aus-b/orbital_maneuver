import numpy as np

# sampling time #
dt = 1.0

# time horizon#
T = 127.2*60.0

# other parameters #
mu = 398600

# initial condition #
r0 = 7778.0
x0 = np.array([r0,0,np.sqrt(mu/(r0**3))])

# Weights #
R = np.array([[10**3.5, 0], [0, 10**3.5]])
S = np.diag([1,1,0,1])

# eIMTR solution #
x_lin = np.array([8085.1, 0.546/60, 0.0, 0.053/60])
u_lin = np.array([0.0004, -0.0038])
psi0 = np.array([-11.93, -54.69, 0, -455009.3])
A = np.array([ [0,1,0,0],
               [x_lin[3]**2+2*mu/(x_lin[0]**3), 0, 0, 2*x_lin[0]*x_lin[3]],
               [0,0,0,0],
               [(2.0*x_lin[1]*x_lin[3]-u_lin[1])/(x_lin[0]**2), -2*x_lin[3]/x_lin[0], 0, -2*x_lin[1]/x_lin[0]]])
B = np.array([[0,0],[1,0],[0,0],[0,1/x_lin[0]]])
