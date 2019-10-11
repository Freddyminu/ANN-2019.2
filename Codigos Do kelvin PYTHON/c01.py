fx = (input('Digite sua função:\n'))
f = lambda x: eval(fx) # pega a função

a = int(input('Digite a: \n')) # pega a e b
b = int(input('Digite b: \n'))

if (f(a)*f(b) < 0):
    print('Iniciando método da bisseção:\n')
    for i in range(1, 101):
        meio = (a+b)/2.0
        if (abs(f(meio)) < 10**-4): # verifica se é menor que 10^-4
            print('f(meio) < 10**-4!')
            break
        else:
            print('Iteração: ' + str(i) + '| a = ' + '{0:.7f}'.format(a) + ' | meio = ' + '{0:.7f}'.format(meio) + '| b = ' + '{0:.7f}'.format(b) + '| f(a) = ' + '{0:.7f}'.format(f(a)) + ' | f(meio) = ' + '{0:.7f}'.format(f(meio)) + '| f(b) = ' + '{0:.10f}'.format(f(b)))
            if f(a)*f(meio) > 0: # critério para fazer do meio = a ou b
                a = meio
            else:
                b = meio
else:
    print('a*b maior que zero! Digite a e b de forma que f(a)*f(b) seja menor que 0')
