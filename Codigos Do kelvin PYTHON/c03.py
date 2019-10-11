# Aluno: Kelvin Welter Bruggmann ANN
# Programa que resolve matrizes nxn e não somente 5x5!

from copy import deepcopy

def linearSolver(A,b): # função que resolve sistemas através da eliminação Gaussiana
    n = len(A) # n = tamanho da matriz
    M = deepcopy(A) # crio uma cópia da matriz para não alterar a original

    print('Método de Eliminação Gaussiana iniciada!')
    for i in range(n):
        for j in range(i+1, n):
            for k in range(n):
                M[j][k] -= M[i][k]*(M[j][k]/M[i][i]) # aqui é onde eu multiplico os elementos da linha que contem o elemento a ser zerado!
        print(M[i]) # printo a minha linha com o elemento já zerado!

    v = deepcopy(b)
    for i in range(n-1, -1, -1):
        v[i] = b[i]/M[i][i] # acho minhas respostas aqui (funciona somente na linha que só tem 1 elemento, depois preciso ir subtraindo os outros elementos que já tenho)
        for j in range(i+1, n):
            v[i]-=(M[i][j]*v[j])/M[i][i] # faço a subtração aqui

    print('\nSolução do sistema:')
    print(v)

# aqui é onde tenho a matriz solução e o sistema linear (preencher no código, sem input)
A = [[3, 2, -4, 2, 5], [2, 3, 3, 1, 4], [5, -3, 1, 2, 4], [5, 2, 4, 1, 3], [1, 5, 2, 3, 4]]
b = [3, 15, 14, 12, 10]
linearSolver(A, b)
