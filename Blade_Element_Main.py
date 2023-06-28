import numpy as np
import prop_input
import matplotlib.pyplot as plt
from scipy import integrate 
from be_calc import be_calc
from prop_plot import prop_plot
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters
'''
Programa construido com base na teoria de Adkins&Liebeck(1994) "Design of Optimum propellers" 
'''

generate_data = 0
# PARÂMETROS DE SIMULAÇÃO DOS PERFIS NO XFOIL
Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list = airfoil_sim_parameters()

if generate_data == 1:
    data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list)


# PARÂMETROS ATMOSFÉRICOS
rho = 1.225  # em kg/m³
mi = 1.7894e-5  # em kg/m.s
v_som = 340  # em m/s

Parameters = prop_input.prop_input()
B = Parameters[0] # Numero de pás
D = Parameters[1] # Diametro da hélice
R = Parameters[2] # Raio da hélice
R_hub = Parameters[3] # Raio do cubo
R_root = Parameters[4] # Raio da região estrutural
RPM = Parameters[5] 
omega = Parameters[6]
Vax = Parameters[7] # Velocidade axial da aeronave
Beta = Parameters[8] # Ângulo de torção geométrica da hélice
nperfil = Parameters[9] # perfil da hélice
# c = Parameters[10] # vetor das cordas em cada posição
pos_c = Parameters[11] # vetor de posição das cordas ao longo do raio
C = Parameters[12] # coef do polinômio de ajuste das cordas,
n = Parameters[13]
P = Parameters[14]

r_step = (R-R_root)/20
i = 0 
r = []
dT_v = []
dQ_v = []
beta_v = []
phi_v =[]
alpha_v =[]
corda_v=[]
a_v = []
a_linha_v = []
Cl_v=[]
r.append(R_root)
while True:
    dT,dQ,corda,beta, phi, a, a_linha,alpha, Cl = be_calc(v_som,mi,rho,r[i],Vax,omega,Beta,nperfil,B,C,R, R_hub)
    dT_v.append(dT)
    dQ_v.append(dQ)
    corda_v.append(corda)
    beta_v.append(beta)
    phi_v.append(phi)
    alpha_v.append(alpha)
    a_v.append(a)
    Cl_v.append(Cl)
    a_linha_v.append(a_linha)
    if r[i]>=R or len(r)==21:
        break
    r.append(r[i]+r_step)
    i=i+1
T = integrate.simpson(dT_v, r)
Q = integrate.simpson(dQ_v, r)
Ct = T/(rho*n**2*D**4)
Cp = Q*omega/(rho*n**3*D**5)
J = Vax/(n*D)
eta = Ct*J/Cp


prop_plot(C, r, R_hub, R_root, beta_v)
plt.figure(2)
plt.plot(r,dT_v,label='dT x r')
plt.legend(loc='best')

plt.figure(3)
plt.plot(r,Cl_v,label='Cl x r')
plt.legend(loc='best')

print('\nTração[N]=', T)
print('\nTorque[N.m]=', Q)
print('\nCt=', Ct)
print('\nCp=', Cp)
print('\neta=', eta)
print('\nbeta=',np.dot(beta_v, 180/np.pi))
print('\nphi=', phi_v)
print('\nalpha=', np.dot(alpha_v, 180/np.pi))
print('\na=',a_v)
print('\na_linha=',a_linha_v)
print('\nraio=',r)
print('\ndT=',dT_v)
print('\nCl=',Cl_v)
plt.show()

