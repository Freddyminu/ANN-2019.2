# Encontre a exponencial f(x) = a*e^bx que melhor se ajusta às seguintes listas de pontos:
import math

n = int(input())
s = input()
x = list(map(float, s.split()))
s = input()
y = list(map(float, s.split()))
for i in range(n):
    if y[i] <= 0:
        print('Necessário fazer a translação!')
    else:
        y[i] = math.log(y[i])
sumx = sum(x)
print('Soma de x: ' + str(sumx))
sumSqrx = sum((i*i) for i in x)
print('Soma de x^2: ' + str(sumSqrx))
sumy = sum(y)
print('Soma de y: ' + str(sumy))
sumxy = 0
for i in range(n):
    sumxy += x[i]*y[i]
print('Soma de x*y: ' + str(sumxy))
a0 = ((sumy * sumSqrx) - (sumxy*sumx))/(n*sumSqrx-sumx*sumx)
a1 = ((n*sumxy) - (sumx*sumy))/(n*sumSqrx-sumx*sumx)
print('a0 = ' + str(a0))
print('a1 = ' + str(a1))
print('a = ' + str(math.exp(a0)))
print('b = ' + str(a1))
