# importa o modulo math e a biblioteca sympy
from sympy import *
init_printing()
import math

x = symbols('x') #define x como variável simbólica.

def f(x):
  return x*exp(x) #cria a função f(x)

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

h = symbols('h')
h = 0.1 # trato h como um símbolo usando sympy
p = 1
Lx = [p, p+h, p+2*h] # coordenadas dos pontos em relacão a x
Ly = [f(p), f(p+h), f(p+2*h)] # coordenadas dos pontos em relacão a y
print("Polinômio de Lagrange calculado: ")
print (Lagrange(Lx, Ly)) # mostra o polinômio de lagrange
print()

def lagrangePoli(x): # crio uma função a partir desse polinômio, copiei e colei o que me foi retornado da função Lagrange
    return -262.502494539829*x - 5.0*E*(-9.99999999999999*x + 11.0) - 9.99999999999999*E*(-5.0*x + 6.0) + 308.673445530231

def fderivada(x):
    return (x + 2)*exp(x) #cria a segunda derivada de f(x)

def erro(p, h):
    return abs(fderivada(p)-lagrangePoli(p)) #função para o erro

# calculo a aproximação com h e depois o erro
for i in range(1, 11): # iterações para os h's pedidos
    if i in [1, 3, 6, 8, 10]:
        print("Com h =", 10**-i, end = ': ')
        print(N(lagrangePoli(1), 10))
        print("Erro = ", N(erro(1, 10**-i),10), end = "\n\n")

print(diff(lagrangePoli(x), x))
