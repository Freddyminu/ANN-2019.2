# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x*exp(x) #cria a função f(x)

def fderivada(x):
    return x*exp(x) + exp(x) #cria a função derivada de f(x)

def formulaDoisPontos(x, h):
    return ((f(x+h) - f(x))/h) # formula dois pontos

def erro(p, h):
    return abs(fderivada(p)-formulaDoisPontos(p, h)) #função para o erro

for i in range(1, 11): # iterações para os h's pedidos
    if i in [1, 3, 6, 8, 10]:
        print("Com h =", 10**-i, end = ': ')
        print(N(formulaDoisPontos(1, 10**-i), 10))
        print("Erro = ", N(erro(1, 10**-i),10), end = "\n\n")
