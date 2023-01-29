# Recebendo parâmetros pelo teclado e passando pra função:

def soma(a, b):
  s = a + b
  print(s)


soma(a = int(input('Digite a: ')) , b = int(input('Digite b: ')))