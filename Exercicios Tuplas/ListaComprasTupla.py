'''Crie um programa que tenha um Tupla única com nomes de produtos e seus respectivos preços na sequência. No final mostre a listagem de preços organizando os dados em forma tabular.'''

listagem = ('Pão', 2, 'Ovos', 12, 'Iogurte', 6, 'Queijo Coalho', 22, 'Queijo Prato', 30, 'Queijo Mussarela', 29.8, 'Presunto', 19.9, 'Bolacha', 5.6, 'Bolo', 15, 'Leite', 4, 'Chá', 6.75, 'Café', 2.5, 'Suco', 5.8, 'Refrigerante (Lata)', 4, 'Agua mineral', 1.5 )

print('-'*40)
print(f'{" Lista de compras na Padaria ":*^40}')
print('-'*40)

for c in range(0, len(listagem)):
  if c % 2 == 0:
    print(f'{listagem[c]:-<30}', end = '')
  else:
    print(f'R$ {listagem[c]:>7.2f}')
