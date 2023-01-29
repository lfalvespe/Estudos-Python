'''Crie um programa onde o usuário poderá digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista ele não será adicionado. No final mostre:

Todos os valores únicos em ordem crescente.

'''

lista = []

while True:
  n = int(input('Digite um valor: '))
  if n not in lista:
    lista.append(n)
    print('Valor adicionado com sucesso!!!')
   
  else:
    print('Valor duplicado, não vou adicionar.')
  o = str(input('Quer continuar? [S/N] '))
  if o in 'Nn':
    break

lista.sort()
print(lista)

# ou 
# print(sorted(lista))



  
  