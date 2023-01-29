''' Crie um programa que calcule o valor a ser pago por um produto considerando seu preço normal e a forma de pagamento:

- Á vista no dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Até 2x no cartão preço normal.
- a partir de 3x no cartão: 20% de juros.

'''

preco = float(input(('Digite o valor do produto R$: ')))

desc = 0

print('')
print(28 * '*')
print('Escolha a forma de pagamento')
print(28 * '*')

print('')
print('1: Dinheiro')
print('2: Cheque')
print('3: Cartão')
print('')

form_pag = int(input('Digite uma opção: '))

print('')


if form_pag == 1 or form_pag == 2:
  desc = - 0.10 * preco   
  preco_final = preco + desc
  
  print('Preço com desconto R$ {}'.format(preco_final))

elif form_pag == 3:
  parc = int(input('Digite o número de parcelas: '))

  if parc == 1:
    desc = - 0.05 * preco
    preco_final = preco + desc
    print('Preço com deconto R$ {}'.format(preco_final))

  elif parc == 2:
    
    print('Preco com desconto R$ {}'.format(preco))

  else:
    desc = 0.2 * preco
    preco_final = preco + desc
    print('Preço com desconto R$ {}'.format(preco_final))
    
  
  
  



