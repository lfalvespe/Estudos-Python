''' Crie um programa que leia o nome e o preço de vários produtos perguntando se o usuário quer continuar. Ao fina mostre:

a) Quantos produtos cadastrados;
b) Quantos produtos custam mais de 1000 reais;
c) Qual o nome do produto mais barato.

'''

o = 's'
cont = 0
tot = 0
maisde1000 = 0
maisbarato = ''
menorpreco = 0

while o in 'Ss':
  
  produto = str(input('Digite o nome do produto: ')).strip()
  preco = int(input('Digite o preço do produto: '))

  tot += preco
  
  if cont == 0:
    menorpreco = preco
    maisbarato = produto
    
  elif preco < menorpreco:
    menorpreco = preco
    maisbarato = produto

  cont += 1
  
  if preco > 1000:  
    maisde1000 += 1

  o = ' '
  
  while o not in 'SsNn':
    o = str(input('Quer cadastrar outro produto [S/N]? ')).strip()

print(f'Total de produtos cadastrados: {cont}')
print(f'Total gasto nas compras: {tot}')
print(f'Total de produtos acima de 1000 reais: {maisde1000}')
print(f'Produto mais barato: {maisbarato}')
  
  