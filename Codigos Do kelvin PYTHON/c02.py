fx = (input('Digite sua função:\n'))
f = lambda x: eval(fx)

fxd = (input('Digite sua função derivada:\n'))
fd = lambda x: eval(fxd)

p = float(input('Digite sua estimativa inicial p1: \n'))

for i in range(1, 101):
    if (abs(f(p)) < 10**-4):
        print('f(p) < 10**-4!')
        break
    else:
        print('Iteração: ' + str(i) + '| pn = ' + '{0:.7f}'.format(p) + ' | f(pn) = ' + '{0:.7f}'.format(f(p)))
        p = p - f(p)/fd(p)
