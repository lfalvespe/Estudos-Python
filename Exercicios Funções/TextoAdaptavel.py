'''Faça um programa que tenha uma função chamada escreva(), que receba um texto como parâmetro e mostre uma mensagem com tamanho adaptável com as linhas abaixo e acima.'''

def escreva(msg):
  print('*'*(len(msg)+4))
  print(f'{msg:^{len(msg)+4}}')
  print('*'*(len(msg)+4))

escreva('Adaptando Textos às linhas')