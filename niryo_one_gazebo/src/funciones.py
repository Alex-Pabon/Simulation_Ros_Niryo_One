#!/usr/bin/env python
#coding:utf-8

import numpy as np
import math
from copy import copy

cos=np.cos; sin=np.sin; pi=np.pi


def dh(d, tetha, a, alfa):
#    """
#    Calcular la matriz de transformacion homogenea asociada 
#    con los parametros
#    de Denavit-Hartenberg.
#    Los valores d, theta, a, alpha son escalares.

#    """
    T = [[math.cos(tetha),-math.cos(alfa)*math.sin(tetha),math.sin(alfa)*math.sin(tetha), a*math.cos(tetha)],
	[math.sin(tetha),math.cos(alfa)*math.cos(tetha),-math.sin(alfa)*math.cos(tetha),a*math.sin(tetha)],
	[0,math.sin(alfa),math.cos(alfa),d],
	[0,0,0,1]]
    return T
    
def fkine_niryo(q):
    """
    Calcular la cinematica directa del robot Niryo One 
    """
    # Longitudes (en metros) - Valores paraNiryo One
    T1 = dh(0.183,q[0],0,math.pi/2)	
    T2 = dh(0,math.pi/2+q[1],0.21,0)
    T3 =dh(0,q[2],0.029973,math.pi/2)
    T4 = dh(0.18,q[3],0,math.pi/2)
    T5 = dh(0,math.pi+q[4],0,(math.pi/2))
    T6 = dh(0.016395,q[5],0,0)

    # Efector final con respecto a la base
    T = np.dot(T1,T2);
    T = np.dot(T,T3);
    T = np.dot(T,T4);
    T = np.dot(T,T5);
    T = np.dot(T,T6);
    return T


def jacobian_niryo(q, delta=0.0001):
    """
    Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]
    """
    # Alocacion de memoria
    J = np.zeros((3,6))
    # Transformacion homogenea inicial (usando q)
    T = fkine_niryo(q)
    #print(T)
    # Iteracion para la derivada de cada columna
    for i in xrange(6):
        # Copiar la configuracion articular inicial
        dq = copy(q);
        # Incrementar la articulacion i-esima usando un delta
	dq[i]= dq[i]+delta
        # Transformacion homogenea luego del incremento (q+dq)
	Td = fkine_niryo(dq) 
        # Aproximacion del Jacobiano de posicion usando diferencias finitas
	J[0][i] = (Td[0][3]-T[0][3])/delta  # x
	J[1][i] = (Td[1][3]-T[1][3])/delta  # y
	J[2][i] = (Td[2][3]-T[2][3])/delta  # z
    return J


def ikine_niryo(xdes, q0):
    """
    Calcular la cinematica inversa de Niryo One numericamente a 
    partir de la configuración articular inicial de q0. 
    """
    epsilon  = 0.001
    epsilon2 = 0.01
    max_iter = 1500
    delta    = 0.00001

    q  = copy(q0)
    Fq = np.zeros(3); #Posición por cinematica directa
    i=0
    #for i in range(max_iter):
    while i < 1:
        # Main loop
	#Se aplica el metodo de Newton 
	F = fkine_niryo(q) #Cinematica directa
	Fq[0] = F[0][3]
	Fq[1] = F[1][3]
	Fq[2] = F[2][3]
	J = jacobian_niryo(q, delta=0.0001) # Jacobiana 
	Jtra = np.transpose(J) #Traspuesta
	J2 = np.dot(J,Jtra) #
	J2 = np.linalg.inv(J2) #Primera inversa
	JI = np.dot(Jtra,J2) #Pseudo inversa
	resta = xdes - Fq
	multi = np.dot(JI,resta)
	if (abs(multi[0]) < epsilon):
		i = 2
	else:
		q = q + multi
    return q


