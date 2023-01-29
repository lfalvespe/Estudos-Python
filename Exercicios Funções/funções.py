def titulo(msg):
  print('-='*20)
  print(f'{msg:^40}')
  print('-='*20)

def soma(a, b):
  
  s = a + b
  return(s)

def produto(a, b):
  p = a * b
  return p

# Main Program

titulo('Funções em Python')
x = soma(3, 4) + produto(3, 4)
print(x)

y = soma(3, 4) * produto(3, 4)
print(y)

z = pow(produto(3, 4), soma(3, 4))
print(z)




