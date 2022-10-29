from multiprocessing import BufferTooShort
import numpy as np
from airfoil_data_get import *
from scipy.optimize import bisect
from phi_bisec import phi_bisec

def be_calc(v_som,mi,rho,r,Vax,omega,beta,nperfil,B,C,R,Cl):
    corda = C(r)
    csi = r/R
    Vr = omega*r  # em m/s
    _lambda = Vax/Vr
    sigma = B*corda/2*np.pi*r

    zeta = 0
    phi = np.arctan(((1+zeta/2)*_lambda/csi)) #phi inicial com zeta=0
    alpha = beta(r)-phi
    # Re = Reynolds_get(Cl, alpha, nperfil)

    W = Vax/np.sin(phi) # chute inicial de velocidade
    Re = W*corda/mi
    Cl_novo,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re) #fazer convergir o Cl novo com o Cl inputado na func


    Cd = Cd+Cdp
    Cy=(Cl*np.cos(phi)-Cd*np.sin(phi)) 
    Cx=(Cl*np.sin(phi)+Cd*np.cos(phi)) 
    K = Cy/(4*(np.sin(phi))**2)
    K_linha = Cx/(4*np.cos(phi)*np.sin(phi))
    phi_t = np.arctan(csi*np.tan(phi))
    f = (B/2)*(1-csi)/np.sin(phi_t)
    F = (2/np.pi)*np.arccos(np.exp(-f))
    a = sigma*K/(F-(sigma*K))
    a_linha = sigma*K_linha/(F+sigma*K_linha)
    phi = np.arctan((Vax*(1+a))/(Vr*(1-a_linha))) #phi final - verificar se está na tolerância com o inicial



    # W = Vax*(1-a)/np.sin(phi)
    dT = 0.5*rho*W**2*B*corda*Cy
    dQ = 0.5*rho*W**2*B*corda*Cx*r
    if (W/v_som)>0.8:
        print('Mach>0.8 quando raio=',r)
    return dT,dQ,corda,beta(r)