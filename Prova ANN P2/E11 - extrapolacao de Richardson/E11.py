N = [[0.9999039012] , [0.999871209] ,
    [0.998733478] , [0.9998634984]]
# pontos errados
grau = 4
b = 1
# b muda e acordo com a ordem, nesse caso ela eh 7 entao... 7 = 7(numero de pontos(Grau))*b logo b = 1..
for i in range (grau - 1):
    for j in range (grau - i - 1):
        N[j].append( ( ( 2**(i*b + b) * N[j + 1][i] ) - N[j][i]) / (2**(i*b + b) - 1) )

print ( 'N %d(1) = %.10f ' % (grau ,N[0][ -1]))
