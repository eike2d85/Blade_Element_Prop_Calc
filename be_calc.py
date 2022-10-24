import numpy as np
from airfoil_data_get import airfoil_data_get
from scipy.optimize import bisect
from phi_bisec import phi_bisec

def be_calc(v_som,mi,rho,r,Vax,omega,alpha,nperfil,B,C,R):
    csi = r/R
    Vr = omega*r  # em m/s
    W = (Vr**2 + Vax**2)**0.5 
    corda = C(r)
    phi = np.arctan(Vax/Vr)  
    _lambda = Vax/Vr
    sigma = B*corda/(2*np.pi*r)
    # phi = np.arctan(_lambda/csi)
    phi_t = np.arctan(csi*np.tan(phi))
    f = (B/2)*(1-csi)/np.sin(phi_t)
    F = (2/np.pi)*np.arccos(np.exp(-f))
    if csi ==1:
        G = 0
    else:
        G = F*np.cos(phi)*np.sin(phi)/_lambda
    # zeta = 2*((np.tan(phi_t)/_lambda) - 1)
    # Re= bisect(Cl_bisec, -1, 3, args=(_lambda, G, Vax, R, zeta,B, mi))
    # Wc = 4*np.pi*_lambda*G*Vax*R*zeta/(Cl*B) 
    Re = rho*corda*W/mi 
    Cl,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re)
    Cd = Cd + Cdp
    # e = Cd/Cl
    Cy=(Cl*np.cos(phi)-Cd*np.sin(phi)) 
    Cx=(Cl*np.sin(phi)+Cd*np.cos(phi)) 
    K = Cy/(4*(np.sin(phi))**2)
    K_linha = Cx/(4*np.cos(phi)*np.sin(phi))
    a = sigma*K/(F-(sigma*K))
    a_linha = sigma*K_linha/(F+sigma*K_linha)
    # phi = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
    # W = Vax*(1+a)/np.sin(phi)
 
    
    # phi = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
    
    dT = 4*np.pi*r*rho*(Vax**2)*(1+a)*a*F
    dQ = 4*np.pi*(r**3)*rho*Vax*omega*(1+a)*a_linha*F
    theta = phi+alpha 
    if (W/v_som)>0.8:
        print('Mach>0.8 quando raio=',r)
    return theta,dT,dQ,corda