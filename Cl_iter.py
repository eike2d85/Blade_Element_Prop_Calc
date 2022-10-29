import numpy as np
from airfoil_data_get import *


def Cl_iter(W, more_data):
    corda = more_data[0]
    alpha = more_data[1]
    nperfil = more_data[2]
    mi = more_data[3]
    Re = W*corda/mi
    Cl_novo,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re) #fazer convergir o Cl novo com o Cl inputado na func
    return W