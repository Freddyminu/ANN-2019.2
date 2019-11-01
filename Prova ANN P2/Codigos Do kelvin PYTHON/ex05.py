# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math
x = symbols('x') #define x como variável simbólica.

def f(x):
  return x**x #cria a função f(x)

def Lagrange (Lx, Ly):
    X=symbols('x')
    if  len(Lx)!= len(Ly): # testa para ver se o número de coordenadas em x bate com y
        print ("ERROR")
        return 1
    y=0 # y será nosso polinômio a ser montado
    for k in range ( len(Lx) ): # percorre as coordenadas em x
        t=1
        for j in range ( len(Lx) ): # a partir das coordenadas em x, percorre y e se y tiver o mesmo indíce de x (não são o mesmo ponto) será adicionado ao polinômio uma nova parte
            if j != k:
                t=t* ( (X-Lx[j]) /(Lx[k]-Lx[j]) ) # cria Li
        y+= t*Ly[k] # adiciona Li ao polinômio
    return y # retorna o polinômio de Lagrange

Lx = [0.99, 1, 1.01] # coordenadas dos pontos em relacão a x
Ly = [f(Lx[0]), f(Lx[1]), f(Lx[2])] # coordenadas dos pontos em relacão a y
print("Polinômio de Lagrange calculado: ")
print (Lagrange(Lx, Ly)) # mostra o polinômio de lagrange
