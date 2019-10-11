# Para cada um dos itens do exercício 6 construa a tabela do método de extrapolação de Richardson e calcule N3(0.1) para
# encontrar uma aproximação com erro pelo menos O(h3) para as derivadas pedidas (extrapole sobre cada uma das N1(h)
# dadas. Use sempre α = 1 e lembre-se de escolher o r corretamente!).

# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x**x #cria a função f(x)

def n3(h, r):
	return ((8*n2(h/r, r) - n2(h, r))/7)

def n2(h, r):
	return ((4*n1(h/r, r) - n1(h, r))/3)

def n1(h, r):
	return formulaDoisPontos(1, h)

def formulaDoisPontos(p, h):
    return ((f(p) - f(p-h))/h) # formula dois pontos

def formulaTresPontos(p, h):
    return ((f(p+h) - f(p-h))/(2*h)) # formula dois pontos

def formulaCincoPontos(p, h):
    return ((f(p-2*h) - 8*f(p-h) + 8*f(p+h) - f(p+2*h))/(12*h)) # formula quatro pontos

print(N(n3(0.1, 3),10))
