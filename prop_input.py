import math
import numpy as np
from scipy.interpolate import CubicSpline
B=2 # Número de Pás
D=1.7526 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.1 # raio do cubo
R_root=0.1524 # raio sem atuação aerodinâmica em m
RPM = 2400 # Velocidade angular em RPM
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
n = RPM/60 #propeller rps
Vax=49.1744 # Velocidade axial em m/s
P = 70*745 # power into propeller
nperfil='NACA4415'
c = np.array([0.104364, 0.14036, 0.130119, 0.108783, 0.085222, 0.058308, 0.01]) # cordas ao longo do raio
beta = np.array([58.3125, 41.8645, 32.2669, 22.2978, 18.7971, 15.9619, 13.8552]) # angulos de torção ao longo do raio
pos_c = np.array([(R_root/R),0.311583,0.449287,0.586957,0.724626,0.86233,1])# posição das cordas em % do raio
pos_c = pos_c * R # posição real das cordas ao longo do raio em m
C = CubicSpline(pos_c, c, bc_type='not-a-knot')
Beta = CubicSpline(pos_c, beta, bc_type='not-a-knot')
#c = C(pos_c) # cordas ao longo do raio após ajuste por spline em m
#beta = Beta(pos_c) # torção ao longo do raio após ajuste por spline em graus


def prop_input():
    Parameters = [B, D, R, R_hub, R_root, RPM, omega, Vax, Beta, nperfil, c, pos_c, C, n, P]
    return Parameters