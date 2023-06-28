import math

def airfoil_data(nperfil, alpha, Re):

    alpha = alpha*180/math.pi # passa para grau

    if nperfil == 'Clark_Y':

        if Re<200000:
            aoa_stall = 10
            Cl = 0.0819*alpha + 0.4887
            Cd = 0.0014*alpha + 0.0133

        else:
            aoa_stall = 12
            Cl = 0.088*alpha + 0.4613
            Cd = 0.0015*alpha + 0.0032


    if nperfil == 'NACA2412':
        aoa_stall = 12
        Cl = 0.093*alpha + 0.3017
        Cd = 0.0037*alpha - 0.0053

   
    return Cl, Cd, aoa_stall