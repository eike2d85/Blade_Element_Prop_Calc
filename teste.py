import numpy as np
from airfoil_data_get import *
from scipy.optimize import bisect

'''
def fixedpoint(func, x0, tolerance, more_data):
    error = 1
    while error > tolerance:
        x = func(x0, more_data)
        error = abs(x0 - x)
        x0 = x
    return x
'''
r = 0.5
R = 1
omega = 2000/60
B=2
beta = 32*np.pi/180
Vax = 5
corda = 0.02
Cl = 0.8
nperfil = 'NACA2412'
rho = 1.225  # em kg/m³
mi = 1.7894e-5  # em kg/m.s
v_som = 340  # em m/s
csi = r/R
Vr = omega*r  # em m/s
_lambda = Vax/Vr
sigma = B*corda/2*np.pi*r
jureg = 0
i = 1
max_iter = 50
Cl_error = 1
Cl_tolerance = 0.005

while Cl_error > Cl_tolerance and i < max_iter:
    if jureg ==0:
        phi = np.arctan(_lambda/csi)
        a = 0
    else:
        a = sigma*K/(F-(sigma*K))
        phi = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
    alpha = beta-phi
    W = Vax*(1-a)/np.sin(phi) 
    Re = W*corda/mi
    Cl_new,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re) # fazer convergir o Cl novo com o Cl inputado 
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
    phi = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
    print(abs(Cl_new-Cl))
    jureg = jureg + 1
    i=i+1



# W = Vax*(1-a)/np.sin(phi)
dT = 0.5*rho*W**2*B*corda*Cy
dQ = 0.5*rho*W**2*B*corda*Cx*r
if (W/v_som)>0.8:
    print('Mach>0.8 quando raio=',r)

print('dT', dT)
print('dQ', dQ)