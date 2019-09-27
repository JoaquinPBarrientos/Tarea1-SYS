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
plt.subplot(2,3,1)
plt.title("Pregunta 1A")
plt.plot(T,lista,'r')

#######################################################################################
# Parte B
# 
print("Ak = 0,616667*j/k")
print("Bk = 0")
# Como Bk es igual a 0 entonces los terminos del coseno no aparecen, es decir, es son igual a 0.

#######################################################################################
#######################################################################################
# Parte C


plt.subplot(2,3,2)
plt.title("Pregunta 1C")
plt.plot(T,lista,'r')

lista2 =[]
K2 = np.arange(1,40,1)
T2 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista2,K2,T2)
plt.subplot(2,3,2)
plt.plot(T2,lista2,'y')

lista3 =[]
K3 = np.arange(1,80,1)
T3 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista3,K3,T3)
plt.subplot(2,3,2)
plt.plot(T3,lista3,'C2')

lista4 =[]
K4 = np.arange(1,160,1)
T4 = np.arange(0,2*np.pi,0.001)
SerieDeFourier(lista4,K4,T4)
plt.subplot(2,3,2)
plt.plot(T4,lista4,'C1')




M_Lista = np.max(lista)
M_Lista2 = np.max(lista2)
M_Lista3 = np.max(lista3)
M_Lista4 = np.max(lista4)

PError1 = M_Lista2 - M_Lista
PError2 = M_Lista3 - M_Lista
PError3 = (M_Lista4 - M_Lista)*100

print("Error")
print("El error más grande es de :",PError3, "%")



#######################################################################################
# Parte D
def SerieDeFourierPromedio (lista,K,T):
	SerieDeFourier(lista,K,T)

	for k in K:
		lista[k] = lista[k]/k

	return lista



lista5 =[]
K5 = np.arange(1,40,1)
T5 = np.arange(0,2*np.pi,0.001)
SerieDeFourierPromedio(lista5,K,T)
plt.subplot(2,3,3)
plt.title("Pregunta 1D")

plt.plot(T5,lista5,'C4')

lista6 =[]
K6 = np.arange(1,80,1)
T6 = np.arange(0,2*np.pi,0.001)
SerieDeFourierPromedio(lista6,K,T)
plt.subplot(2,3,3)
plt.plot(T6,lista6,'C9')


lista7 =[]
K7 = np.arange(1,160,1)
T7 = np.arange(0,2*np.pi,0.001)
SerieDeFourierPromedio(lista7,K,T)
plt.subplot(2,3,3)
plt.plot(T7,lista7,'C11')
plt.legend(('k = 40', 'k = 80', 'k = 160'))
# Nos podemos dar cuenta que al graficar los promedios, dan los mismos valores, por lo que se sobreponen las funciones y no se puede ver dos de las tres,
# EN otras palabras, los valores dan lo mismo en las 3 funciones a pesar de el K elegido. 
# Por lo tanto el error es igual a 0.
#######################################################################################
# PREGUNTA 2
#A.1 
# y[0] = 1 , 
# y[n] = 1 + alpha*y[n-1] Para todo n≥1.

#######################################################################################
#A.2
 
alpha = [1/2,1/3,7/8]

# lista con valores
x = 1 # Para todo n≥0.
N = np.arange(1,20,1)
n = np.arange(0,20,1)

def sangre(valores,e):
	for n in N:
		y = x + alpha[e]*valores[n-1] 
		valores.append(y)
	return valores


lista_alpha0=[1]
sangre(lista_alpha0,0)
plt.subplot(2,3,4)
plt.title("Pregunta 2.A.2(alpha = 1/2)")
plt.stem(n,lista_alpha0)

lista_alpha1=[1]
sangre(lista_alpha1,1)
plt.subplot(2,3,5)
plt.title("Pregunta 2.A.2(alpha = 1/3)")
plt.stem(n,lista_alpha1)

N = np.arange(1,50,1)
n = np.arange(0,50,1)
lista_alpha2=[1]
sangre(lista_alpha2,2)
plt.subplot(2,3,6)
plt.title("Pregunta 2.A.2(alpha = 7/8)")
plt.stem(n,lista_alpha2)

#######################################################################################
#A.3
#  PARA alpha = 1/2 ----> lim n->00 y[n] = 2
#  PARA alpha = 1/3 ----> lim n->00 y[n] = 1.5
#  PARA alpha = 7/8 ----> lim n->00 y[n] = 8









plt.subplot_tool() # Esto abre una ventana para poder visualizar mejor los graficos, puedes ajustarlos como quieras.


plt.show()