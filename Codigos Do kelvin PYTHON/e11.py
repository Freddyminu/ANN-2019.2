# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

// nao eh a 13 de 2019.2 no casoo.....

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x*exp(x) #cria a função f(x)

def fderivada(x):
    return x*exp(x)+exp(x) # cria a função derivada de f(x)

def formulaTresPontos(x, h):
    return ((f(x+h) - f(x-h))/(2*h)) # cria a função para a formula de 3 pontos

def erro(p, h):
    return abs(fderivada(p)-formulaTresPontos(p, h)) # retorna a fórmula do erro

for i in range(1, 11): # iterações para os h's pedidos
    if i in [1, 3, 6, 8, 10]:
        print("Com h =", 10**-i, end = ': ')
        print(N(formulaTresPontos(1, 10**-i), 10))
        print("Erro = ", N(erro(1, 10**-i),10), end = "\n\n")
