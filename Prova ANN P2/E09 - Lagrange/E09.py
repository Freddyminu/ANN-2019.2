Xi = [ i/10 for i in range( -50 ,25 ,5) ]
Yi = [-2.26,-3.97,-0.86,-4.36,4.46,
  3.23,-0.64,1.05,0.23,2.99,
  3.22,0.1,3.3,-2.9,-2.24]

grau = len(Yi)
Ai = [ 1 for i in range(grau) ]

for i in range(grau):
  t = 1
  for j in range(grau):
      if i != j:
          t *= (Xi[i]-Xi[j])
  Ai[i] = Yi[i]/t
for i in range(grau):
  print("a%d : %.15f"%(i,Ai[i]))
