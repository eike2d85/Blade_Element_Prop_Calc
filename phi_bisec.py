import numpy as np
from scipy.optimize import bisect
from Cl_bisec import Cl_bisec
from airfoil_data_get import airfoil_data_get


def phi_bisec(phi,csi,_lambda,nperfil,alpha,Vax,R,B,mi,sigma,Vr):
    phi_t = np.arctan(csi*np.tan(phi))
    f = (B/2)*(1-csi)/np.sin(phi_t)
    F = (2/np.pi)*np.arccos(np.exp(-f))
    if csi ==1:
        G = 0
    else:
        G = F*np.cos(phi)*np.sin(phi)/_lambda
    zeta = 2*((np.tan(phi_t)/_lambda) - 1)
    Re= bisect(Cl_bisec, -1, 3, args=(_lambda, G, Vax, R, zeta,B, mi))
    Cl,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re)
    Cd = Cd + Cdp
    # e = Cd/Cl
    Cy=(Cl*np.cos(phi)-Cd*np.sin(phi)) 
    Cx=(Cl*np.sin(phi)+Cd*np.cos(phi)) 
    K = Cy/(4*(np.sin(phi))**2)
    K_linha = Cx/(4*np.cos(phi)*np.sin(phi))
    a = sigma*K/(F-(sigma*K))
    a_linha = sigma*K_linha/(F+sigma*K_linha)
    phi_correct = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
    W = Vax*(1+a)/np.sin(phi)

    return W