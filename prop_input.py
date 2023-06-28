import math
import numpy as np
from scipy.interpolate import CubicSpline

B=3 # Número de Pás
D=0.5 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.035 # raio do cubo
R_root=0.055 # raio sem atuação aerodinâmica em m
RPM = 5500 # Velocidade angular em RPM
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
n = RPM/60 #propeller rps
Vax=15# Velocidade axial em m/s
P = 700 # power into propeller
nperfil='NACA2412'

c = np.array([0.0297,	0.0386,	0.0254,	0.0121]) # cordas ao longo do raio
beta = np.array([40.1009,	19.8197,	12.7752,	9.7171]) # angulos de torção ao longo do raio
pos_c = np.array([(R_root/R), 0.4, 0.7, 1])# posição das cordas em % do raio


'''
B=2 # Número de Pás
D=0.5 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.035 # raio do cubo
R_root=0.055 # raio sem atuação aerodinâmica em m
RPM = 5500 # Velocidade angular em RPM
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
n = RPM/60 #propeller rps
Vax=15# Velocidade axial em m/s
P = 700 # power into propeller
nperfil='NACA2412'

c = np.array([0.0226,	0.0501,	0.0311,	0.0052]) # cordas ao longo do raio
beta = np.array([27.2407,	21.1164,	16.1944,	10.2543]) # angulos de torção ao longo do raio
pos_c = np.array([(R_root/R), 0.4, 0.7, 1])# posição das cordas em % do raio

'''

'''
B=2 # Número de Pás
D=0.5 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.035 # raio do cubo
R_root=0.055 # raio sem atuação aerodinâmica em m
RPM = 5500 # Velocidade angular em RPM
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
n = RPM/60 #propeller rps
Vax=15# Velocidade axial em m/s
P = 700 # power into propeller
nperfil='NACA2412'

c = np.array([0.03511,	0.03941,	0.02649,	0.01596]) # cordas ao longo do raio
beta = np.array([32.4485,	24.1839,	14.0549,	15.122]) # angulos de torção ao longo do raio
pos_c = np.array([(R_root/R), 0.4, 0.7, 1])# posição das cordas em % do raio
'''

'''

B=2 # Número de Pás
D=1.7526 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.1 # raio do cubo
R_root=0.1524 # raio sem atuação aerodinâmica em m
RPM = 2400 # Velocidade angular em RPM
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
n = RPM/60 #propeller rps
Vax=49.1744# Velocidade axial em m/s
P = 70*745 # power into propeller
nperfil='NACA4415'

c = np.array([0.10436352, 0.1403604, 0.13011912, 0.10878312, 0.08522208, 0.05830824, 0]) # cordas ao longo do raio
beta = np.array([58.3125, 41.8645, 32.2669, 22.2978, 18.7971, 15.9619, 13.8552]) # angulos de torção ao longo do raio
pos_c = np.array([(R_root/R), 0.311582609, 0.449286957, 0.586956522, 0.724626087, 0.862330435, 1])# posição das cordas em % do raio

'''
pos_c = pos_c * R # posição real das cordas ao longo do raio em m
C = CubicSpline(pos_c, c, bc_type='not-a-knot')
Beta = CubicSpline(pos_c, beta, bc_type='not-a-knot')



def prop_input():
    Parameters = [B, D, R, R_hub, R_root, RPM, omega, Vax, Beta, nperfil, c, pos_c, C, n, P]
    return Parameters





