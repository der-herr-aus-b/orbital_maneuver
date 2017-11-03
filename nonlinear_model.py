from init import *

def f(x,u):
    out = np.zeros(3)
    out[0] = x[1]
    out[1] = x[0]*x[2]**2 - mu/x[0]/x[0] + u[0]
    out[2] = (-2*x[2]*x[1] + u[1])/x[0]
    return out
