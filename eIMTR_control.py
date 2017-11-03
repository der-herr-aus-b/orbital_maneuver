from init import *
import scipy.linalg as la

def eIMTR_control(t):
    psi = la.expm(np.transpose(A)*(-t)).dot(psi0)
    invR = np.linalg.inv(R)
    u = -invR.dot(np.transpose(B).dot(psi))
    return u
