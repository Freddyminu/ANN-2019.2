N = [[19.08222025061125] , [17.764812318813924] ,
    [ 17.441751852770494] , [17.361200124395396] ,
    [ 17.34107242927712] , [17.336041095748442]]

grau = 6
b = 2

for i in range (grau - 1):
    for j in range (grau - i - 1):
        N[j].append( ( ( 2**(i*b + b) * N[j + 1][i] ) - N[j][i]) / (2**(i*b + b) - 1) )

print ( 'N %d(1) = %.10f ' % (grau ,N[0][ -1]))

# diferencias finitas, extrapolacao de richardsao, spline, integral dupla(meio ponto), romberg, lagarange
# Simpson, diferencias divididas.
# spline cubica 5 questao vale 3 pontos
