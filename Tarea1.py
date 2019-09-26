import math
import matplotlib.pyplot as plt
import numpy as np
import scipy
from sympy import symbols, Function

def SerieDeFourier (lista,K,T):
	for t in T:
		y = 0
		for k in K:

			 y += (np.sin(k*t)/k)
		lista.append(y)
		
	return lista



######################################################################################
# PREGUNTA 1
# Parte A
lista =[]
K = np.arange(1,30,1)
T = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista,K,T)
plt.subplot(3,1,1)
plt.plot(T,lista,'r')

#######################################################################################
# Parte B
#######################################################################################
#######################################################################################
# Parte C


plt.subplot(3,1,2)
plt.plot(T,lista,'r')

lista2 =[]
K2 = np.arange(1,40,1)
T2 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista2,K2,T2)
plt.subplot(3,1,2)
plt.plot(T2,lista2,'y')

lista3 =[]
K3 = np.arange(1,80,1)
T3 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista3,K3,T3)
plt.subplot(3,1,2)
plt.plot(T3,lista3,'C2')

lista4 =[]
K4 = np.arange(1,160,1)
T4 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista4,K4,T4)
plt.subplot(3,1,2)
plt.plot(T4,lista4,'C1')




M_Lista1 = np.max(lista)
M_Lista2 = np.max(lista2)
M_Lista3 = np.max(lista3)
M_Lista4 = np.max(lista4)


print("Errores")


#######################################################################################
# Parte D
def SerieDeFourierPromedio (lista,K,T):
	SerieDeFourier(lista,K,T)

	for k in K:
		lista[k] = lista[k]/k

	return lista




lista5 =[]
K5 = np.arange(1,500,1)
T5 = np.arange(0,2*np.pi,0.001)

SerieDeFourierPromedio(lista5,K,T)
plt.subplot(3,1,3)
plt.plot(T5,lista5,'C6')

#######################################################################################

plt.show()