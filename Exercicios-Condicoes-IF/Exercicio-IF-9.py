''' Crie um programa para aprovar ou não um empréstimo bancário para compra de uma casa. Pergunte o valor do salário, o valor da casa e em quantos anos quer pagar. Calcule o valor da prestação mensal sabendo que não pode exceder 30% do salário senão o empréstimo é negado. '''

sal = float(input('Informe o valor do seu salário: '))
preco = float(input('Informe o preço da casa: '))
prazo = int(input('Informe o prazo do financiamento em anos: '))

prest = preco/(prazo*12)
limite = 0.3 * sal

if prest <= limite:
  print('Empréstimo aprovado.')
  print('Valor da prestação: {}'.format(prest))

else:
  print('Empréstimo não aprovado. Valor da prestação excede 30% do seu salário')
  print('Valor da prestação: {}'.format(prest))