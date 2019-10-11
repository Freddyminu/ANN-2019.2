# Encontre a parábola f(x) = a0 + a1x + a2x^2 que melhor se ajusta às seguintes listas de pontos:

def linearSolver(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass

   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]
          print(M)

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  print(x)

n = int(input())
s = input()
x = list(map(float, s.split()))
s = input()
y = list(map(float, s.split()))

# somas de x, x^2, x^3, x^4
sumx = sum(x)
sumSqrx = sum((i*i) for i in x)
sumCubex = sum((i*i*i) for i in x)
sumQuartax = sum((i*i*i*i) for i in x)
print('Soma de x: ' + str(sumx))
print('Soma de x^2: ' + str(sumSqrx))
print('Soma de x^3: ' + str(sumCubex))
print('Soma de x^4: ' + str(sumQuartax))

# somas de y, y*x, y*x^2
sumy = sum(y)
sumxy = 0
for i in range(n):
    sumxy += x[i]*y[i]
sumySqrx = 0
for i in range(n):
    sumySqrx += x[i]*x[i]*y[i]
print('Soma de y: ' + str(sumy))
print('Soma de x*y: ' + str(sumxy))
print('Soma de x*x*y: ' + str(sumySqrx))

A = [[n, sumx, sumSqrx], [sumx, sumSqrx, sumCubex], [sumSqrx, sumCubex, sumQuartax]]
b = [sumy, sumxy, sumySqrx]
linearSolver(A, b)
