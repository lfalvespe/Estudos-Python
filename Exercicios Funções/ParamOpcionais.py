# Parâmetros opcionais - permite que passe menos parâmetros do 
# que a função pede. Quando não informa recebe o valor padrão.

def soma(a = 0, b = 0, c = 0):
  s = (a+b+c)
  print(s)


soma(1, 3, 5)
soma(1, 2)
soma(8)
soma(a = 2, b = 3)
soma(a = 4, c = 15)
soma(c = 3, a = 10)