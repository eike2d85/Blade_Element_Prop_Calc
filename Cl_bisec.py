from airfoil_data_get import airfoil_data_get
import numpy as np

def Cl_bisec(Cl,_lambda, G, Vax, R, zeta,B, mi):
    Wc = 4*np.pi*_lambda*G*Vax*R*zeta/(Cl*B) #não dá p usar o Cl antes de calcular... e agora???

    Re = Wc/mi 
    

    return Re