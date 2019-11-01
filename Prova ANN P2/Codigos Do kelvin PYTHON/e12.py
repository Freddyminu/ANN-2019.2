# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x*exp(x) #cria a função f(x)

def fderivada(x):
    return x*exp(x)+exp(x) # derivada de f(x)

def formulaCincoPontos(p, h):
    return ((f(p-2*h) - 8*f(p-h) + 8*f(p+h) - f(p+2*h))/(12*h))

def erro(p, h):
    return abs(fderivada(p)-formulaCincoPontos(p, h))

for i in range(1, 11): # iterações para os h's pedidos
    if i in [1, 3, 6, 8, 10]:
        print("Com h =", 10**-i, end = ': ')
        print(N(formulaCincoPontos(1, 10**-i), 10)) # função N para transformar a expressão em um double com precisão = 10
        print("Erro = ", N(erro(1, 10**-i),10), end = "\n\n")
