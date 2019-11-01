# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x*exp(x) #cria a função f(x)

def fderivada(x):
    return (x + 2)*exp(x) # define a segunda derivada de f(x)

def derivada(funcao):
  return diff(f(x),x) #derivada da função f(x)

def formulaTresPontos(p, h):
    return ((f(p-h) - 2*f(p) + f(p+h))/(h*h)) # retorna o valor obtido na formula de 3 pontos

def erro(p, h):
    return abs(fderivada(p)-formulaTresPontos(p, h)) # função para cálculo do erro

for i in range(1, 11): # iterações para os h's pedidos
    if i in [1, 3, 6, 8, 10]:
        print("Com h =", 10**-i, end = ': ')
        print(N(formulaTresPontos(1, 10**-i), 10))# função N para transformar a expressão em um double com precisão = 10
        print("Erro = ", N(erro(1, 10**-i),10), end = "\n\n")
