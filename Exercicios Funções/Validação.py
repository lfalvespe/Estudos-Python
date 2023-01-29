'''Crie um programa uq etnha uma função chamada leiaInt() que só receba um valor dse for numérico e exiba na tela.'''


def leiaInt(msg):
  ok = False
  valor = 0
  
  while True:
    n = str(input(msg))
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print('Erro. Digite um número válido!!!')
  
    if ok: 
      break
  
  return valor

#Programa principal

n = leiaInt('Digite um número: ')
print(f'Você digitou o valor {n}')