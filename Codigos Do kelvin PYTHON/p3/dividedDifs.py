import numpy as np

def difsDivididas(x,y):
    m = len(x)
    x = np.copy(x)
    a = np.copy(y)
    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(x[k:m] - x[k-1])
    return a

n = int(input('Número de pontos: '))
x = []
y = []
for i in range(n):
    x.append(float(input('Ponto em X: ')))
    y.append(float(input('Ponto em Y: ')))
print(difsDivididas(x, y))
