# Em cada um dos itens a seguir, use as fórmulas de aproximação para aproximar f'(p).
# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return exp(-x**2) #cria a função f(x)

def formulaDoisPontos(p, h):
    return ((f(p) - f(p-h))/h) # formula dois pontos

def formulaTresPontos(p, h):
    return ((f(p+h) - f(p-h))/(2*h)) # formula dois pontos

def formulaCincoPontos(p, h):
    return ((f(p-2*h) - 8*f(p-h) + 8*f(p+h) - f(p+2*h))/(12*h)) # formula quatro pontos

l = [0.1, 0.05, 0.025]

for h in l:
	print(f'i = {h}')
	print(N(formulaDoisPontos(1, h), 10))
	print(N(formulaTresPontos(1, h), 10))
	print(N(formulaCincoPontos(1, h), 10))
	print()
