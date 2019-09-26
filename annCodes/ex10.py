# Integração usando regra dos trapézios e encontrando h através de um n dado

import math

print('NÃO ESQUEÇA DE DEFINIR SUA FUNÇÃO')
a = float(input('Digite seu a: '))
# b = float(input('Digite seu b: '))
b = math.pi/2
n = float(input('Digite n: '))
h = (b-a)/n

ponto = a
aprox = 0
print('Pontos usados no cálculo: ')
while ponto <= b:
    print('Ponto: ' + str(ponto), end = ' ')
    print('f(ponto) = ' + str(math.sin(ponto)))
    if ponto != a and ponto != b:
        aprox += 2*(math.sin(ponto))
    else:
        aprox += math.sin(ponto)
    ponto += h
aprox = aprox*(h/2)
print('Aproximação encontrada = ' + str(aprox))
