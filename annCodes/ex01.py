# Encontre a reta r(x) = a0 +a1x que melhor se ajusta às seguintes listas de pontos:
n = int(input())
s = input()
x = list(map(float, s.split()))
s = input()
y = list(map(float, s.split()))
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
